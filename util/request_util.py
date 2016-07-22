# coding=utf-8
from sys import path
path.append(r"./util")
import json_util,requests,md_five,json,check

_setting = "data/conf/setting.json"
_headers = {
    "Content-Type": "application/json;charset=UTF-8"
}

# 设置参数中的密码
def set_password(params):
    if params.has_key("password"):
        params["password"] = md_five.encrypt(md_five.encrypt(params.get("password")) + params.get("curTime"))
    if params.has_key("paymentPassword"):
        params["password"] = md_five.encrypt(params.get("paymentPassword"))
    return params

# 发送接口测试请求
def request(url,method,params):
    result = None
    if method.lower() == "get":
        result = requests.get(url,headers=_headers)
    elif method.lower() == "post":
        result = requests.post(url,headers=_headers,data=json.dumps(set_password(params)))
    else :
        raise Exception("请求方法异常！")
    return result

# 测试接口入口
def fasttest(json,att):
    # 获取请求数据
    test_data = json_util.read(json,att)
    url = test_data.get("url")
    method = test_data.get("method")
    params = test_data.get("request")
    check_data = test_data.get("check")

    # 获取setting数据
    host = json_util.read(_setting,"host")
    port = json_util.read(_setting,"port")

    # 拼接完整的url
    url = "http://" + host + ":" + str(port) + "/" + url

    # 获取请求结果
    result = request(url,method,params)
    rcode = result.status_code
    assert rcode == 200
    assert check.assert_body(result.text, check_data) == True
    # print rcode == 200
    # print check.assert_body(result.text, check_data) == True
