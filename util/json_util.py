# coding=utf-8
import json

# 获取json文件的attribute节点数据
def read(fileStr,attribute):
    str = file(fileStr)
    return json.load(str).get(attribute)

def cycle(json):
    for a in json.keys():
        print json.get(a)
