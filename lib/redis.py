from lib.sdk.geetest_config import GEETEST_ID, GEETEST_KEY, REDIS_HOST, REDIS_PORT, CYCLE_TIME, BYPASS_URL, GEETEST_BYPASS_STATUS_KEY
from lib.sdk.geetest_lib import GeetestLib
import redis, requests, json, time

# 建立redis连接池
def init_redis_connect():
    try:
        host = REDIS_HOST
        port = REDIS_PORT
        pool = redis.ConnectionPool(host=host, port=port)
        redis_connect = redis.Redis(connection_pool=pool)
        return redis_connect
    except Exception as e:
        return None


redis_connect = init_redis_connect()


# 发送bypass请求，获取bypass状态并进行缓存（如何缓存可根据自身情况合理选择,这里是使用redis进行缓存）
def check_bypass_status():
    while True:
        response = ""
        params = {"gt": GEETEST_ID}
        try:
            response = requests.get(url=BYPASS_URL, params=params)
        except Exception as e:
            print(e)
        if response and response.status_code == 200:
            #print(response.content)
            bypass_status_str = response.content.decode("utf-8")
            bypass_status = json.loads(bypass_status_str).get("status")
            redis_connect.set(GEETEST_BYPASS_STATUS_KEY, bypass_status)
        else:
            bypass_status = "fail"
            redis_connect.set(GEETEST_BYPASS_STATUS_KEY, bypass_status)
        #print("bypass状态已经获取并存入redis，当前状态为-{}".format(bypass_status))
        time.sleep(CYCLE_TIME)


# 从缓存中取出当前缓存的bypass状态(success/fail)
def get_bypass_cache():
    bypass_status_cache = redis_connect.get(GEETEST_BYPASS_STATUS_KEY)
    bypass_status = bypass_status_cache.decode("utf-8")
    return bypass_status