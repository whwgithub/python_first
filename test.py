#!/usr/bin/python
# coding=utf-8

import json

import datetime
import time


gval1=1
gval2=2
def methon():
    try:
        1 / 0
    except ArithmeticError, e:
        raise ArithmeticError("算术异常", e)
    return ""


def methon2():
    return methon()

def methon3():
    return methon2()

if __name__ == "__main__":
    # inputStr = raw_input("请输入:")
    # print inputStr
    # for i in [1, 2, 3]:
    #     print "循环次数:", i
    #     try:
    #         methon3()
    #     except  Exception, e:
    #         print "异常了：",e
    #         continue
    e = "ERROR: ('http://localhost:8080/user-values/loyalty/data', 'orgName=%E7%94%9F%E6%B4%BB%E7%94%B5%E5%99%A8%E4%BA%8B%E4%B8%9A%E9%83%A8&segments=%E7%82%8A%E5%85%B7&interval=200&percentile=97&manualCache=True', error(10054, ''))"
    if "10054" in e or "10061" in e or "104" in e:
        print "网络异常..."