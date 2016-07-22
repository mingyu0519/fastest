# coding=utf-8
from sys import path,_getframe
path.append(r"./util")
import request_util

LOGIN_JSON = "data/login.json"

def test_login():
    "登录"
    request_util.fasttest(LOGIN_JSON, _getframe().f_code.co_name)
def test_login_password_error():
    "登录密码错误"
    request_util.fasttest(LOGIN_JSON, _getframe().f_code.co_name)
