from app import db
from flask_login import UserMixin

class Admin(db.Model,UserMixin):
    user_id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    username = db.Column(db.String(30),nullable=False)
    password = db.Column(db.String(128),nullable=False)
    is_active = db.Column(db.Integer)
    
    # 表格更名
    __tablename__ = 'admin'
    # 初始化每个实例。（若在第6步导入DBO文件，可不用写以下初始化语句，DBO类方法中已封装。）
    def __init__(self ,username, password):
        self.username = username
        self.password = password
        self.is_active = 1

    def __repr__(self):
        return '<Admin user_id=%r>' % self.user_id
    
    # flask_login 登录所需
    def get_id(self):
        return str(self.user_id)
    
    def is_admin(self):
        return 1
