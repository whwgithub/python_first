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


# 用户特征带参数缓存

def sendRequest(posturl, postData, headers):
    try:
        postData = urllib.urlencode(postData)
        request = urllib2.Request(posturl, postData, headers)
        response = urllib2.urlopen(request)
        text = response.read()
    except urllib2.URLError, e:
        print urllib2.URLError(posturl, postData, e)
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
    # 用户整体分析参数
    overview_param = {
        "orgName": "",
        "segment1Name": "",
        "segment2Name": "",
        "productModel": '',
        "manualCache": True
    }
    # 用户购买分析
    buy_analytics_param = {
        "orgName": '',
        "segments": '',
        "segment": '',
        "productModel": '',
        "province": '',
        "cityLevel": '',
        "city": '',
        "county": '',
        "startTime": '',
        "endTime": '',
        "buyNumLow": '',
        "buyNumHight": '',
        "buyMoneyLow": '',
        "buyMoneyHigh": '',
        "platform": '',
        "manualCache": True
    }
    # 用户安装分析
    install_analytics_param = {
        "orgName": '',
        "segments": '',
        "segment": '',
        "productModel": '',
        "province": '',
        "cityLevel": '',
        "city": '',
        "county": '',
        "startTime": '',
        "endTime": '',
        "buyNumLow": '',
        "buyNumHight": '',
        "buyMoneyLow": '',
        "buyMoneyHigh": '',
        "platform": '',
        "manualCache": True
    }
    # 用户保养分析
    upkeep_analytics_param = {
        "orgName": '',
        "segments": "",
        "segment": "",
        "productModel": '',
        "province": '',
        "cityLevel": "",
        "city": '',
        "county": '',
        "startTime": '',
        "endTime": '',
        "num_low": "",
        "num_high": "",
        "manualCache": True
    }
    # 用户维修分析
    service_analytics_param = upkeep_analytics_param
    # 用户咨询分析
    consult_analytics_param = upkeep_analytics_param
    # 用户投诉分析
    complaints_analytics_param = upkeep_analytics_param

    # 各个请求的url和参数定义
    # 用户特征 - 用户整体分析
    overview_module = ["base", "segment", "base_userArea", "base_lastYear", "base_userSleep", "business"]
    overview = []
    for module in overview_module:
        overview_param["module"] = module
        tmp = [
            "/user-overview/overview/" + module,
            overview_param
        ]
        overview.append(tmp)

    # 用户特征 - 用户购买分析
    buy_analytics_module = ["buy_amount", "buy_lastYearTrend", "buy_lastYearTrend_new", "buy_last15Trend",
                            "buy_time", "price", "platform", "area", "buy_product_segment", "buy_product_model",
                            "buy_freq", "buy_money", "buy_value"]
    buy_analytics = []
    for module in buy_analytics_module:
        buy_analytics_param["module"] = module
        tmp = [
            "/user-overview/buy-analytics/" + module,
            buy_analytics_param
        ]
        buy_analytics.append(tmp)

    # 用户特征 - 用户安装分析
    install_analytics_module = ["install_amount", "install_lastYear", "install_lastYearNew", "area",
                                "install_product_segment", "install_product_model", "install_frequents"]
    install_analytics = []
    for module in install_analytics_module:
        install_analytics_param["module"] = module
        tmp = [
            "/user-overview/install-analytics/" + module,
            install_analytics_param
        ]
        install_analytics.append(tmp)

    # 用户特征 - 用户保养分析
    upkeep_analytics_module = ["userKeep_num", "userKeep_lastYear", "userKeep_lastYearTrend", "area",
                               "userKeep_product_segment", "userKeep_product_model", "userKeep_frequents"]
    upkeep_analytics = []
    for module in upkeep_analytics_module:
        upkeep_analytics_param["module"] = module
        tmp = [
            "/user-overview/upkeep-analytics/" + module,
            upkeep_analytics_param
        ]
        upkeep_analytics.append(tmp)

    # 用户特征 - 用户维修分析
    service_analytics_module = ["userService_num", "userService_lastYear", "userService_lastYearTrend", "area",
                                "duration", "userService_product_segment", "userService_product_model",
                                "userService_frequents"]
    service_analytics = []
    for module in service_analytics_module:
        service_analytics_param["module"] = module
        tmp = [
            "/user-overview/service-analytics/" + module,
            service_analytics_param
        ]
        service_analytics.append(tmp)

    # 用户特征 - 用户咨询分析
    consult_analytics_module = ["consult_num", "consult_lastYear", "consult_lastYearTrend", "area",
                                "consult_product_segment", "consult_product_model", "consult_frequents"]
    consult_analytics = []
    for module in consult_analytics_module:
        consult_analytics_param["module"] = module
        tmp = [
            "/user-overview/consult-analytics/" + module,
            consult_analytics_param
        ]
        consult_analytics.append(tmp)

    # 用户特征 - 用户投诉分析
    complaints_analytics_module = ["complaint_num", "complaint_lastYear", "complaint_lastYearTrend", "area",
                                   "emergency", "complaint_product_segment", "complaint_product_model",
                                   "complaint_frequents"]
    complaints_analytics = []
    for module in complaints_analytics_module:
        complaints_analytics_param["module"] = module
        tmp = [
            "/user-overview/complaints-analytics/" + module,
            complaints_analytics_param
        ]
        complaints_analytics.append(tmp)

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

    overview_param_list = get_org_param_list(overview_param)
    buy_analytics_param_list = get_org_param_list(buy_analytics_param)
    install_analytics_param_list = get_org_param_list(install_analytics_param)
    upkeep_analytics_param_list = get_org_param_list(upkeep_analytics_param)
    service_analytics_param_list = get_org_param_list(service_analytics_param)
    consult_analytics_param_list = get_org_param_list(consult_analytics_param)
    complaints_analytics_param_list = get_org_param_list(complaints_analytics_param)

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


    overview_cond = get_label_Analysis_cond(overview_param_list, overview)
    buy_analytics_cond = get_label_Analysis_cond(buy_analytics_param_list, buy_analytics)
    install_analytics_cond = get_label_Analysis_cond(install_analytics_param_list, install_analytics)
    upkeep_analytics_cond = get_label_Analysis_cond(upkeep_analytics_param_list, upkeep_analytics)
    service_analytics_cond = get_label_Analysis_cond(service_analytics_param_list, service_analytics)
    consult_analytics_cond = get_label_Analysis_cond(consult_analytics_param_list, consult_analytics)
    complaints_analytics_cond = get_label_Analysis_cond(complaints_analytics_param_list, complaints_analytics)

    # 装箱所有请求url和参数
    request_url_all = [
        overview_cond,
        buy_analytics_cond,
        install_analytics_cond,
        upkeep_analytics_cond,
        service_analytics_cond,
        consult_analytics_cond,
        complaints_analytics_cond
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


# 开始发生请求
print "开始发起[用户特征]cache请求..."
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

print "cache[用户特征]请求结束. 共发送[", reqCont, "]个请求. 耗时:", (datetime.datetime.now() - start_time).seconds,"秒"
