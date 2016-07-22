# coding=utf-8
from sys import path,_getframe
path.append(r"./util")
import json_util,json,types,sys
reload(sys)
sys.setdefaultencoding('utf-8')

# 检查服务器返回结果
def assert_body(actual, expect):
    bool_data = True
    for ekey in expect.keys():
        if type(expect.get(ekey)) == types.UnicodeType :
            expect_bool = '"{0}":"{1}"'.format(ekey.encode("utf-8"),expect.get(ekey).encode("utf-8")) in actual
        elif type(expect.get(ekey)) == types.IntType:
            expect_bool = '"{0}":{1}'.format(ekey,expect.get(ekey)) in actual
        elif type(expect.get(ekey)) == types.BooleanType:
            if expect.get(ekey) == True:
                expect_bool = '"{0}":{1}'.format(ekey,"true") in actual
            else:
                expect_bool = '"{0}":{1}'.format(ekey,"false") in actual
        else:
            raise Exception("预期结果数据类型异常！")
        bool_data = bool_data and expect_bool
    if bool_data == False:
        print "实际返回：",actual
        print "预期返回：",json.dumps(expect,ensure_ascii=False,indent=4)
    return bool_data

# assert_body(json_util.read("./util/test.json","a"),json_util.read("./util/test.json","b"))
