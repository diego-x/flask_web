import re
from flask import render_template, Blueprint, request, url_for,redirect ,session ,make_response, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user,login_required,logout_user,current_user
from lib.sdk.geetest_lib import GeetestLib
import json , os

from lib.redis import check_bypass_status,get_bypass_cache
from lib.sdk.geetest_config import GEETEST_ID, GEETEST_KEY

user = Blueprint('user', __name__ , template_folder="../templates/" )

from app import db , WEB_ROOT
from .models import Users
from .models import Picture


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


@user.route("/")
def index_page():
    return redirect('/user/index/1',code=302)

@user.route("/index/<page>")
def index(page=0):
     # 页数转化验证
    try:
        page = int(page)
    except:
        return render_template("404.html")
    
    # 每页20条记录
    picture_info = Picture.query.offset((page - 1) * 20).limit(20)
    count = Picture.query.count()
    print(count)
    pictures = []
    for picture in picture_info:
        pictures.append(picture.get_picture_info())

    username = ""
    if hasattr(current_user, "username"):
        username = current_user.username
        
    return render_template("user_index.html" , pictures = pictures , count = count //20 + 1 , username = username)

# 用户登录
@user.route("/user_login" , methods=['POST' , 'GET'])
def user_login():
    
    if request.method == "POST":

        # 验证码验证
        if validate() != 1 :
            res = make_response(json.dumps({"stat" : -1 , "data" : "验证码错误或过期"}))
            res.headers["Content-Type"] = "text/json"
            return res
        
        name = request.values.get("username")
        password = request.values.get("password")
        # 用户角色区分
        session["role"] = "user"
        if name and password :
            res = Users.query.filter_by(username = name).first()

            if res and check_password_hash(res.password ,password) :
                # 采用flask_login 进行登录验证 
                user = Users(res.username,res.password)
                login_result = login_user(res)

                if login_result == True :
                    res = make_response(json.dumps({"stat" : 1 , "data" : "登录成功"}))
                    res.headers["Content-Type"] = "text/json"
                    return res
                else :
                    res = make_response(json.dumps({"stat" : -1 , "data" : "内部错误，联系管理员"}))
                    res.headers["Content-Type"] = "text/json"
                    return res
            else: 
                res = make_response(json.dumps({"stat" : -1 , "data" : "用户名或密码错误"}))
                res.headers["Content-Type"] = "text/json"
                return res
        else:
            res = make_response(json.dumps({"stat" : -1 , "data" : "用户名或密码不能为空"}))
            res.headers["Content-Type"] = "text/json"
            return res
    else :
        return render_template("user_login.html")

# 用户注册
@user.route("/user_reg" , methods=['POST', 'GET'])
def user_reg():
    
    if request.method == "POST":

        # 验证码验证
        if validate() != 1 :
            res = make_response(json.dumps({"stat" : -1 , "data" : "验证码错误或过期"}))
            res.headers["Content-Type"] = "text/json"
            return res

        # 用户注册
        name = request.values.get("username")
        password = request.values.get("password")
        repassword = request.values.get("repassword")
        if name and password and repassword:
            if password != repassword :
                res = make_response(json.dumps({"stat" : -1 , "data" : "密码不一致"}))
                res.headers["Content-Type"] = "text/json"
                return res
            
            # 检测是否为重复用户名
            res = Users.query.filter_by(username = name).first()
            if res != None :
                res = make_response(json.dumps({"stat" : -1 , "data" : "用户已注册"}))
                res.headers["Content-Type"] = "text/json"
                return res
            # reg
            password = generate_password_hash(password)
            sql = Users(username = name, password = password)
            db.session.add(sql)
            db.session.commit()
            db.session.close()
            
            res = make_response(json.dumps({"stat" : 1 , "data" : "注册成功"}))
            res.headers["Content-Type"] = "text/json"
            return res
        else:
            res = make_response(json.dumps({"stat" : 1 , "data" : "用户名或密码不能为空"}))
            res.headers["Content-Type"] = "text/json"
            return res
    else:
        return render_template("user_reg.html")


# 图片下载
@user.route("/download/<pid>" , methods=['GET'])
@login_required
def download(pid):
    try:
        pid = int(pid)
        picture = Picture.query.filter_by(picture_id = pid).first()
    except:
        return "404"
    
    if picture != None :
        filename = os.path.basename(picture.real_Path)
        response = make_response(send_from_directory(WEB_ROOT + '/static/upload/' ,filename.encode('utf-8').decode('utf-8'),as_attachment=True))
        response.headers["Content-Disposition"] = "attachment; filename={}".format(filename.encode().decode('latin-1'))
        return response
    else:
        return "图片不存在"



# 前端登录检查
@user.route("/loginCheck" , methods=['GET'])
@login_required
def login_check():
    res = make_response(json.dumps({"login_status" : 1}))
    res.headers["Content-Type"] = "text/json"
    return res


@user.route("/show/<pid>", methods=["GET"])
def show(pid = 0):
    # name = request.values.get("username")
    try :
        pid = int(pid)
        picture = Picture.query.filter_by(picture_id = pid).first()
        
        # 获取当前图片的前后图
        pictures = Picture.query.all()
        picture_index = pictures.index(picture)
        
        if picture_index == 0 :
            picture_next = pictures[picture_index + 1]
            picture_last = None
        elif picture_index == len(pictures) -1 :
            picture_next = None
            picture_last = pictures[picture_index - 1]
        else:
            picture_next = pictures[picture_index + 1]
            picture_last = pictures[picture_index - 1]
    except :
        return render_template("404.html")
    
    username = ""
    if hasattr(current_user, "username"):
        username = current_user.username
    
    return render_template("user_showPicture.html",picture = picture, username = username , picture_next = picture_next, picture_last = picture_last)


# 安全退出
@user.route("/logout" , methods=['GET'])
@login_required
def logout():
    logout_user()
    return redirect('/user/index/1',code=302)
