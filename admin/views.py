from flask import render_template, Blueprint, request, url_for,redirect ,make_response,session
from hashlib import md5
from werkzeug.utils import secure_filename
from PIL import Image
import time ,random ,json,os
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user,login_required,logout_user,current_user

from lib.redis import check_bypass_status,get_bypass_cache
from lib.sdk.geetest_config import GEETEST_ID, GEETEST_KEY
from lib.sdk.geetest_lib import GeetestLib

admin = Blueprint('admin', __name__)

from user.models import Picture
from admin.models import Admin
from app import STATIC_FILE_PATH, db ,WEB_ROOT

# 验证码验证
def validate():
    challenge = request.form.get(GeetestLib.GEETEST_CHALLENGE, None)
    validate = request.form.get(GeetestLib.GEETEST_VALIDATE, None)
    seccode = request.form.get(GeetestLib.GEETEST_SECCODE, None)
    bypass_status = get_bypass_cache()
    gt_lib = GeetestLib(GEETEST_ID, GEETEST_KEY)
    if bypass_status == "success":
        result = gt_lib.successValidate(challenge, validate, seccode)
    else:
        result = gt_lib.failValidate(challenge, validate, seccode)
    # 注意，不要更改返回的结构和值类型
    if result.status == 1:
        return 1
    else:
        return 0
    
# 管理员判断
def isAdmin():
    if hasattr(current_user, "is_admin"):
        return True
    return False

@admin.route('/uploadFile')
@login_required
def index():
    return render_template("admin_upload.html")

@admin.route('/admin_login', methods = ["GET", "POST"])
def admin_login():
    if request.method == "POST":
        
        # 验证码验证
        if validate() != 1 :
            res = make_response(json.dumps({"stat" : -1 , "data" : "验证码错误或过期"}))
            res.headers["Content-Type"] = "text/json"
            return res
        session["role"] = "admin"
        username = request.values.get("username")
        password = request.values.get("password")
        
        if username and password :
            
            res = Admin.query.filter_by(username = username).first()
            if res and check_password_hash(res.password ,password) :
                
                login_result = login_user(res)
                print(current_user)
                if login_result == True :
                    return "登录成功"
        
        return "登录失败"
        
    return render_template("admin_login.html")

# 添加图片
@admin.route('/upload', methods = ["POST"])
@login_required
def upload():
    
    if isAdmin() == False : return "非法访问"
    
    #响应信息
    message = ""
    code = 0
    file_url = ""
    uploadPath = STATIC_FILE_PATH + "upload/"
    
    file = request.files.get("file")
    title = request.values.get("title")
    
    if file and title :
        # 获取并检测后缀
        ext = file.filename.split('.')[-1]
        accessList = ['jpg', 'png', 'jpeg', 'gif', 'bmp']
        if ext in accessList :
                
            tmp_name = md5(secure_filename(file.filename).encode()).hexdigest() + "." + ext
            file.save(uploadPath  + tmp_name)
            downloadUrl = "/static/upload/" + tmp_name
            real_Path = downloadUrl
            # 图片放入数据库
            current_time = time.ctime()
            
            # 获取图片尺寸
            img = Image.open(uploadPath  + tmp_name)
            chang = img.size[0]
            kuan =  img.size[1]
            size  = "{0}  x  {1}".format(img.size[0], img.size[1])
            print(img.size)
            
            #生成缩略图
            img.thumbnail(( int(chang/kuan) * 500 , 500))
            tmp_name = md5(str(random.randint(1,9999999)).encode()).hexdigest()
            img.save(STATIC_FILE_PATH + 'user/bizhi/' + tmp_name + ".png", "PNG")
            index_src = '/static/user/bizhi/'+ tmp_name + ".png"
            
            # # 裁剪图片
            # print(img.size)
            # img1 = Image.open(STATIC_FILE_PATH + 'user/bizhi/'+ tmp_name + ".png")
            # chang1 = (img1.size[0]-450)/2
            # res = img1.crop((chang,0, chang + 450 ,img1.size[1]))
            # print(res.size)
            # res.save(STATIC_FILE_PATH + 'user/bizhi/' + tmp_name + ".png", "PNG")
            
            # 放入数据库
            picture = Picture(title, index_src , real_Path ,size, downloadUrl , current_time)
            db.session.add(picture)
            db.session.commit()
            db.session.close()
            
            file_url = index_src
            message = "上传成功"
            code = 1
        else :
            message = "不允许的后缀"
    else:
        message = "缺少必要的参数"
    
    res = make_response(json.dumps({"code" : code , "file_url": file_url, "msg" : message}))
    res.headers["Content-Type"] = "text/json"
    return res

# 展示管理界面
@admin.route('/imageManager', methods = ["GET"])
@login_required
def imageManager():
    if isAdmin() == False : return "非法访问"
    pictures = Picture.query.all()
    count = Picture.query.count()
    return render_template("admin_manager.html" , count = count , pictures = pictures)


# 删除图片
@admin.route('/deleteImg', methods = ["POST"])
@login_required
def delImg():
    
    if isAdmin() == False : return "非法访问"
    message = ""
    code = 0
    
    picture_id = request.values.get("pid")
    picture = Picture.query.filter_by(picture_id = picture_id).first()
    
    if picture != None :
        # 删除缩略图
        if os.path.isfile(picture.index_src ) == True :
            os.remove(WEB_ROOT + picture.index_src)
        # 删除图片
        if os.path.isfile(picture.real_Path ) == True :
            os.remove(WEB_ROOT + picture.real_Path)
        
        # 从数据库中删除
        db.session.delete(picture)
        db.session.commit()
        db.session.close()
        
        message = "删除成功"
        code = 1

    else:
        message = "图片不存在"
        
    res = make_response(json.dumps({"code" : code ,  "msg" : message}))
    res.headers["Content-Type"] = "text/json"
    return res


# 修改图片标题
@admin.route('/modifyImg', methods = ["POST"])
@login_required
def modifyImg():
    
    if isAdmin() == False : return "非法访问"
    message = ""
    code = 0
    
    title = request.values.get("title")
    picture_id = request.values.get("pid")
    
    picture = Picture.query.filter_by(picture_id = picture_id).first()
    
    if picture != None :
        picture.title = title
        db.session.commit()
        db.session.close()
        
        message = "更新成功"
        code = 1
    else:
        message = "图片不存在"
    
    res = make_response(json.dumps({"code" : code ,  "msg" : message}))
    res.headers["Content-Type"] = "text/json"
    return res


@admin.route('/logout', methods = ["GET"])
def logout():
    logout_user()
    return redirect(url_for('admin.admin_login'),code=302)