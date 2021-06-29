from app import db
import json
from flask_login import UserMixin

class Users(db.Model,UserMixin):
    
    user_id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    username = db.Column(db.String(30),nullable=False)
    password = db.Column(db.String(128),nullable=False)
    is_active = db.Column(db.Integer)
    
    # 表格更名
    __tablename__ = 'users'
    
    # 初始化每个实例。（若在第6步导入DBO文件，可不用写以下初始化语句，DBO类方法中已封装。）
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.is_active = 1

    def __repr__(self):
        return '<Users userid=%r>' % self.user_id
    
    # flask_login 登录所需
    def get_id(self):
        return str(self.user_id)
    
    # 返回json格式的用户信息
    def get_user_info(self):
        data = {}
        if self.user_id :
            data.update({"user_id" : self.user_id })
        if self.username :
            data.update({"username" : self.username })
        return json.dumps(data)
    

class Picture(db.Model):
    
    picture_id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    title = db.Column(db.String(30),nullable=False)
    index_src = db.Column(db.String(128),nullable=False)
    real_Path = db.Column(db.String(128),nullable=False)
    downloadurl = db.Column(db.String(200),nullable=False)
    size = db.Column(db.String(50))
    time = db.Column(db.String(50))
    
    # 表格更名
    __tablename__ = 'picture'
    
    __table_args__ = {'mysql_engine': 'InnoDB', 'mysql_charset': 'utf8'} 

    
    def __init__(self, title, index_src, real_Path, size, downloadurl, time):
        self.title = title
        self.index_src = index_src
        self.real_Path = real_Path
        self.size = size
        self.downloadurl = downloadurl
        self.time = time
    
    def __repr__(self):
        return '<Picture picture_id=%r>' % self.picture_id
    
    # 返回json格式的图片信息
    def get_picture_info(self):
        data = {}
        if self.picture_id :
            data.update({"picture_id" : self.picture_id })
        if self.title :
            data.update({"title" : self.title })
        if self.real_Path :
            data.update({"real_Path" : self.real_Path })
        if self.downloadurl :
            data.update({"downloadurl" : self.downloadurl })
        if self.index_src :
            data.update({"index_src" : self.index_src })
        if self.size :
            data.update({"size" : self.size })
        if self.time :
            data.update({"time" : self.time })
        return data
    
    #GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY 'diego2333' WITH GRANT OPTION;