from  flask  import Flask ,session ,make_response
from flask.templating import render_template
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

import os

# 静态目录
STATIC_FILE_PATH = os.getcwd() + '/static/'
WEB_ROOT = os.getcwd() + "/"
app =  Flask(__name__ , static_folder = STATIC_FILE_PATH , static_url_path = '/static')

# 开启csrf 保护
csrf = CSRFProtect()
csrf.init_app(app)

# 基本配置文件
app.config['SECRET_KEY'] = os.urandom(24)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://*'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_POOL_SIZE'] = 500
app.config['SQLALCHEMY_POOL_RECYCLE'] = 10

# 数据库连接(生成一个数据库操作对象)
db = SQLAlchemy(app, use_native_unicode='utf8')


# 请求建立前
@app.before_request
def before_request():
    #print(db.session)
    pass

# 请求结束后 操作处理
@app.teardown_request
def teardown_request(exception):
    # 关闭数据库连接
    db.session.close()



# 登录保护
login_manager = LoginManager(app)
login_manager.init_app(app)
login_manager.login_view = 'app1.show_login'
login_manager.login_message = '请登入！！' # 默认的错误消息是
login_manager.login_message_category = 'info' # 设置闪现的错误消息的类别


# 注册该蓝图  登入注册蓝图
from user.views import user
from admin.views import admin
from code.views import code

app.register_blueprint(user, url_prefix='/user/')
app.register_blueprint(admin, url_prefix='/admin/')
app.register_blueprint(code, url_prefix='/code/')


from user.models import Users
from admin.models import Admin

# login_user的回调函数，登录保护必须包含
@login_manager.user_loader
def load_user(user_id):
    role = session.get("role")
    if role == "admin":
        return Admin.query.filter_by(user_id = user_id).first()
    elif role == "user":
        return Users.query.filter_by(user_id = user_id).first()

# 未授权访问统一处理接口
@login_manager.unauthorized_handler
def unauthorized():
    res = make_response({"stat": 0 ,"data" : "未登录"})
    res.status = "200"
    res.headers["Content-Type"] = "text/json"
    return res

# 异常页面统一处理
@app.errorhandler(400)
def csrf_error(e):
    res = make_response({"stat": 0 ,"data" : "csrf_token 错误 重新刷新网页"})
    res.status = "200"
    res.headers["Content-Type"] = "text/json"
    return res

#404 
@app.errorhandler(404)
def not_found(e):
    return render_template("404.html")

# 数据库创建
db.create_all()

@app.route("/")
def index():
    return "1"


if __name__ == "__main__" :
    app.run("0.0.0.0",80)