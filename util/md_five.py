# coding=utf-8
import hashlib

# 字符串加密为md5
def encrypt(str):
    hashmd5 = hashlib.md5()
    hashmd5.update(str)
    md5_str = hashmd5.hexdigest()
    return md5_str
