#!/usr/bin/python
# coding=utf-8

import cookielib
import urllib
import urllib2


def sendRequest(posturl, postData, headers):
    postData = urllib.urlencode(postData)
    request = urllib2.Request(posturl, postData, headers)
    response = urllib2.urlopen(request)
    text = response.read()
    return text


def sendQuery(url, postData):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:14.0) Gecko/20100101 Firefox/14.0.1'}
    text = sendRequest(url, postData, headers)
    return text


def login(hosturl, username, password):
    posturl = hosturl + '/login'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:14.0) Gecko/20100101 Firefox/14.0.1',
               'Referer': posturl}
    postData = {
        'userName': username,
        'password': password
    }

    text = sendRequest(posturl, postData, headers)
    return text


def init():
    cj = cookielib.LWPCookieJar()
    cookie_support = urllib2.HTTPCookieProcessor(cj)
    opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)
    urllib2.install_opener(opener)
    h = urllib2.urlopen(hosturl)


if __name__ == "__main__":
    # hosturl = 'http://10.73.37.63:8080'
    hosturl = 'http://localhost:8080'

    init()

    login(hosturl, "zhongsf", "123456")

    # 封装所有请求url和参数,

