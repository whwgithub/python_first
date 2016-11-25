#!/usr/bin/python  
# coding=utf-8

import cookielib
import copy
import json
import urllib
import urllib2
import datetime
import sys

reload(sys)
sys.setdefaultencoding("utf-8")


# 用户挖掘带参数缓存

def sendRequest(posturl, postData, headers):
    try:
        postData = urllib.urlencode(postData)
        request = urllib2.Request(posturl, postData, headers)
        response = urllib2.urlopen(request)
        text = response.read()
    except Exception, e:
        raise Exception(posturl, postData, e)
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

    # 请求参数定义
    # 用户价值与忠诚度
    loyalty_param = {
        # "orgName": "",
        # "segments": "",
        "interval": "200",
        "percentile": "97",
        "manualCache": True
    }
    # 用户价值详情检索
    value_search_param = {
        # "orgName": "",
        # "segments": "",
        "sumBuyAmountLow": "",
        "sumBuyAmountHigh": "",
        "sumBuyCountLow": "",
        "sumBuyCountHigh": "",
        "manualCache": True
    }

    # 各个请求的url和参数定义
    # 用户挖掘 - 用户价值与忠诚度
    user_values_loyalty = [
        "/user-values/loyalty/data",
        loyalty_param
    ]
    # 用户挖掘 - 用户价值详情检索
    user_values_value_search = [
        "/marketing-tools/user-search/value-search",
        value_search_param
    ]


    # 获取事业部-产品大类-产品小类
    def getSeg():
        orgUserSegUrl = hosturl + '/util/org-user-seg'
        orgUserUrl = hosturl + '/util/org-user'
        orgUserSeg = json.loads(sendQuery(orgUserSegUrl, ''))
        orgUser = json.loads(sendQuery(orgUserUrl, ''))
        orgUserTemp = orgUser['data']
        orgUserSegTemp = orgUserSeg['data']
        result = {}
        for value in orgUserTemp:
            for key, second in value.iteritems():
                secondList = []
                for th in second:
                    for value1 in orgUserSegTemp:
                        for x in value1:
                            if x == th:
                                secondList.append(value1)
                result[key] = secondList
        return result


    # 根据事业部-产品大类-产品小类组合查询条件
    def get_org_param_list(param_dic):
        labels = getSeg()
        org_param_list = []
        for key, value in labels.iteritems():
            param_tmp = copy.copy(param_dic)
            if key != "集团总部":
                param_tmp["orgName"] = key
            # if param_tmp not in org_param_list:
            org_param_list.append(param_tmp)
            for value1 in value:
                for key1, value2 in value1.iteritems():
                    param_tmp2 = copy.copy(param_tmp)
                    param_tmp2["segments"] = key1
                    # if param_tmp2 not in org_param_list:
                    org_param_list.append(param_tmp2)
        return org_param_list


    loyalty_param_list = get_org_param_list(loyalty_param)
    value_search_param_list = get_org_param_list(value_search_param)


    # print "overview_param_list.len=", len(overview_param_list)
    # for l in overview_param_list:
    #     print l

    # 根据事业部-产品大类-产品小类获取标签分析查询url
    def get_label_Analysis_cond(param_list, label_Analysis):
        label_Analysis_cond = []
        for param in param_list:
            if isinstance(label_Analysis[0], list):
                for label in label_Analysis:
                    label_Analysis_tmp2 = [label[0], param]
                    label_Analysis_cond.append(label_Analysis_tmp2)
            else:
                label_Analysis_tmp = [label_Analysis[0], param]
                label_Analysis_cond.append(label_Analysis_tmp)
        return label_Analysis_cond


    user_values_loyalty_cond = get_label_Analysis_cond(loyalty_param_list, user_values_loyalty)
    user_values_value_search_cond = get_label_Analysis_cond(value_search_param_list, user_values_value_search)

    # 装箱所有请求url和参数
    request_url_all = [
        user_values_loyalty_cond,
        user_values_value_search_cond,
    ]


# 发生请求方法
def sendReq(sendReqs):
    start_time = datetime.datetime.now()
    action = sendReqs[0]
    postData = sendReqs[1]
    url = hosturl + action
    text = sendQuery(url, postData)
    print "请求url:", url, "耗时:", (datetime.datetime.now() - start_time).seconds, "秒, 返回数据长度:", \
        len(text), "请求参数:", postData
    # print "请求url:",url, "请求参数:", postData


# 开始发生请求
print "开始发起[用户挖掘]cache请求..."
start_time = datetime.datetime.now()
reqCont = 0
for requests in request_url_all:
    try:
        if isinstance(requests[0], list):
            for reqs in requests:
                try:
                    req = reqs[0]
                    if isinstance(req, list):
                        pass
                    else:
                        sendReq(reqs)
                        reqCont += 1
                except Exception, e:
                    print "ERROR:", e
                    if "10054" in repr(e) or "10061" in repr(e) or "104" in repr(e):
                        print "网络异常..."
                        sys.exit(1)
                    continue
        else:
            sendReq(requests)
            reqCont += 1
    except Exception, e:
        print "ERROR:", e
        if "10054" in repr(e) or "10061" in repr(e) or "104" in repr(e):
            print "网络异常..."
            sys.exit(1)
        continue

print "cache[用户挖掘]请求结束. 共发送[", reqCont, "]个请求. 耗时:", (datetime.datetime.now() - start_time).seconds, "秒"
