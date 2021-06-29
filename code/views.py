import json
import time
import redis
import requests
import threading
from flask import Flask, request, Response, jsonify,Blueprint,render_template

from lib.sdk.geetest_config import GEETEST_ID, GEETEST_KEY, REDIS_HOST, REDIS_PORT, CYCLE_TIME, BYPASS_URL, GEETEST_BYPASS_STATUS_KEY
from lib.sdk.geetest_lib import GeetestLib

from lib.redis import check_bypass_status,get_bypass_cache

code = Blueprint('code', __name__, template_folder="../templates/")



thread = threading.Thread(target=check_bypass_status)
thread.start()
code.secret_key = GeetestLib.VERSION

@code.route("/")
def index():
    return render_template("code_index.html")

# 验证初始化接口，GET请求
@code.route("/register", methods=["GET"])
def first_register():
    # 必传参数
    #     digestmod 此版本sdk可支持md5、sha256、hmac-sha256，md5之外的算法需特殊配置的账号，联系极验客服
    # 自定义参数,可选择添加
    #     user_id 客户端用户的唯一标识，确定用户的唯一性；作用于提供进阶数据分析服务，可在register和validate接口传入，不传入也不影响验证服务的使用；若担心用户信息风险，可作预处理(如哈希处理)再提供到极验
    #     client_type 客户端类型，web：电脑上的浏览器；h5：手机上的浏览器，包括移动应用内完全内置的web_view；native：通过原生sdk植入app应用的方式；unknown：未知
    #     ip_address 客户端请求sdk服务器的ip地址
    bypass_status = get_bypass_cache()
    gt_lib = GeetestLib(GEETEST_ID, GEETEST_KEY)
    digestmod = "md5"
    user_id = "test"
    param_dict = {"digestmod": digestmod, "user_id": user_id, "client_type": "web", "ip_address": "127.0.0.1"}
    if bypass_status == "success":
        result = gt_lib.register(digestmod, param_dict)
    else:
        result = gt_lib.local_init()
    # 注意，不要更改返回的结构和值类型
    return Response(result.data, content_type='application/json;charset=UTF-8')


# 二次验证接口，POST请求
@code.route("/validate", methods=["POST"])
def second_validate():
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
        response = {"result": "success", "version": GeetestLib.VERSION}
    else:
        response = {"result": "fail", "version": GeetestLib.VERSION, "msg": result.msg}
    return jsonify(response)
