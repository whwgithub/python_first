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


# 左边菜单所有页面缓存(不带参数)&用户标签带参数缓存

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
    # 标签示意
    tag_cloud_param = {
        "orgName": '',
        "segments": "",
        "segment": "",
        "model": '',
        "startTime": "",
        "endTime": '',
        "manualCache": True
    }
    # 标签分析
    label_analysis_param = {
        "orgName": '',
        "segments": '',
        "segment": '',
        # "models": '',
        # "labels": '',
        "relation": "or",
        "manualCache": True
    }
    # 用户价值与忠诚度
    loyalty_param = {
        "orgName": "",
        "segments": "",
        "interval": "200",
        "percentile": "97",
        "manualCache": True
    }
    # 用户价值详情检索
    value_search_param = {
        "orgName": "",
        "segments": "",
        "sumBuyAmountLow": "",
        "sumBuyAmountHigh": "",
        "sumBuyCountLow": "",
        "sumBuyCountHigh": "",
        "manualCache": True
    }
    # 用户搜索引擎
    search_user_param = {
        "orgName": "",
        "segments": "",
        "segment": "",
        # "model": '',
        # "province": '',
        # "city": '',
        # "county": '',
        "fetchBuyInfo": False,
        # "buyStartTime": '',
        # "buyEndTime": '',
        # "platform": '',
        "businessType": "",
        # "businessStartTime": '',
        # "businessEndTime": '',
        "exceptbusType": "",
        # "exceptbusStartTime": '',
        # "exceptbusEndTime": '',
        "cityLevel": "",
        "userArea": "",
        "jobcharacte": "",
        "motorhomes": "",
        "familys": "",
        "likefavors": "",
        "usertypes": "",
        "userValueName": "",
        "complains": "",
        "repairs": "",
        "activityjoins": "",
        # "userLabel": '',
        # "exceptUserLabel": '',
        # "name": '',
        # "mobile": '',
        "labelIds": "",
        "exceptLabelIds": "",
        # "relation": '',
        "labelRelation": "or",
        # "inputAddress": '',
        "range": 0.0,
        # "buyPlatform": '',
        "manualCache": True
    }
    # 产品推荐引擎
    potential_users_param = {
        "orgName": "",
        "segment1Name": "",
        "segment2Name": "",
        "productLevel": "",
        "productFunc": "",
        # "productNeed": 'null',
        # "province": 'null',
        # "city": 'null',
        # "county": 'null',
        "cityLevel": "",
        "userArea": "",
        "productComplain": "",
        "productRepair": "",
        "activityjoins": "",
        "jobcharacte": "",
        "motorhomes": "",
        "familys": "",
        "likefavors": "",
        "usertypes": "",
        "manualCache": True
    }
    # 各个请求的url和参数定义, 1: 代表启用,0: 代表不启用
    # 首页地域分布
    home_area_data = [
        "/home/area-data",
        {"manualCache": True}
    ]
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

    # 用户标签 - 标签介绍 - 标签示意(云图)
    label_Analysis_tag_cloud = [
        "/user-tags/tag-introduction/tag-cloud",
        tag_cloud_param
    ]
    # 用户标签 - 标签分析 - 标签规模分析
    label_Analysis_scale = [
        "/user-labels/label-Analysis/scale/labelAll",
        label_analysis_param
    ]
    # 用户标签 - 标签分析 - 购物特征分析
    label_Analysis_buyFeature_module = ["buyCount", "onlineBuyCount", "buyCategory", "buyPrice",
                                        "buyType", "buyPsychology", "buyPromotionPrefer"]
    label_Analysis_buyFeature = []
    for module in label_Analysis_buyFeature_module:
        label_analysis_param["module"] = module
        tmp = [
            "/user-labels/label-Analysis/buyFeature/" + module,
            label_analysis_param
        ]
        label_Analysis_buyFeature.append(tmp)

    # 用户标签 - 标签分析 - 产品偏好分析
    label_Analysis_productLevel_module = ["productLevel", "productFunction"]
    label_Analysis_productLevel = []
    for module in label_Analysis_productLevel_module:
        label_analysis_param["module"] = module
        tmp = [
            "/user-labels/label-Analysis/ProductPrefer/" + module,
            label_analysis_param
        ]
        label_Analysis_productLevel.append(tmp)

    # 用户标签 - 标签分析 - 渠道偏好分析
    label_Analysis_ChannelPrefer_module = ["buyChannelPrefer", "buyShopCount", "buyInternetCount",
                                           "buyPlatformCount"]
    label_Analysis_ChannelPrefer = []
    for module in label_Analysis_ChannelPrefer_module:
        label_analysis_param["module"] = module
        tmp = [
            "/user-labels/label-Analysis/ChannelPrefer/" + module,
            label_analysis_param
        ]
        label_Analysis_ChannelPrefer.append(tmp)

    # 用户标签 - 标签分析 - 时间偏好分析
    label_Analysis_TimePrefer_module = ["buyPromotionPerfer", "buyPromotionDayPrefer", "buyTimePrefer"]
    label_Analysis_TimePrefer = []
    for module in label_Analysis_TimePrefer_module:
        label_analysis_param["module"] = module
        tmp = [
            "/user-labels/label-Analysis/TimePrefer/" + module,
            label_analysis_param
        ]
        label_Analysis_TimePrefer.append(tmp)

    # 用户标签 - 标签分析 - 群体结构分析
    label_Analysis_Groups_module = ["buyGroupsCity", "buyGroupsCounty", "buyGroupsAge", "buyGroupsStablity",
                                    "buyGroupsIncome", "buyGroupsUserTypes", "buyGroupsJob", "buyGroupsCars",
                                    "buyGroupsFamily", "buyGroupsLifePrefer", "buyGroupsInterest", "buyGroupsHabits"]
    label_Analysis_Groups = []
    for module in label_Analysis_Groups_module:
        label_analysis_param["module"] = module
        tmp = [
            "/user-labels/label-Analysis/Groups/" + module,
            label_analysis_param
        ]
        label_Analysis_Groups.append(tmp)

    # 用户标签 - 标签分析 - 用户价值分析
    label_Analysis_userValues_module = ["userValue", "userValueConsumeAblity", "userValueLoyal", "userValueActiveness"]
    label_Analysis_userValues = []
    for module in label_Analysis_userValues_module:
        label_analysis_param["module"] = module
        tmp = [
            "/user-labels/label-Analysis/userValues/" + module,
            label_analysis_param
        ]
        label_Analysis_userValues.append(tmp)

    # 用户标签 - 标签分析 - 网络特征分析
    label_Analysis_NetFeature_module = ["netActivity", "netFlow", "netMobile", "netWorkDay", "newWeekDay"]
    label_Analysis_NetFeature = []
    for module in label_Analysis_NetFeature_module:
        label_analysis_param["module"] = module
        tmp = [
            "/user-labels/label-Analysis/NetFeature/" + module,
            label_analysis_param
        ]
        label_Analysis_NetFeature.append(tmp)

    # 用户标签 - 标签分析 - 用户需求分析
    label_Analysis_userNeed_module = ["userNeedAirCondition", "userNeedKitchen", "userNeedWashMachine",
                                      "userNeedFridge", "userNeedLifeElectric", "userNeedWaterHeaters",
                                      "userNeedEnvEquipment"]
    label_Analysis_userNeed = []
    for module in label_Analysis_userNeed_module:
        label_analysis_param["module"] = module
        tmp = [
            "/user-labels/label-Analysis/userNeed/" + module,
            label_analysis_param
        ]
        label_Analysis_userNeed.append(tmp)

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
    # 画像工具 - 用户搜索引擎
    user_search_searchUser = [
        "/marketing-tools/user-search/searchUser",
        search_user_param
    ]

    # # 画像工具 - 用户搜索引擎 - 目标用户分析
    label_Analysis_targetUser_module = ["targetUserLabel", "buyFreqAttribute", "userValueAttribte",
                                        "buyCategoryAttribute", "buyTypeAttribute", "productLevelPrefer",
                                        "buyChannelPrefer", "homeAndCarAttribute", "userLifePreferAttribute",
                                        "userContact", "userValueActiveness"]
    label_Analysis_targetUser = []
    for module in label_Analysis_targetUser_module:
        search_user_param["module"] = module
        tmp = [
            "/marketing-tools/user-search/targetUser-Analysis/" + module,
            search_user_param
        ]
        label_Analysis_targetUser.append(tmp)

    # 画像工具 - 产品推荐引擎
    potential_users_search = [
        "/marketing-tools/potential-users/search",
        potential_users_param
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
    labels = getSeg()
    label_analysis_param_list = []
    for key, value in labels.iteritems():
        label_analysis_param_tmp = copy.copy(label_analysis_param)
        label_analysis_param_tmp["orgName"] = key
        # if label_analysis_param_tmp not in label_analysis_param_list:
        label_analysis_param_list.append(label_analysis_param_tmp)
        for value1 in value:
            for key1, value2 in value1.iteritems():
                label_analysis_param_tmp2 = copy.copy(label_analysis_param_tmp)
                label_analysis_param_tmp2["segments"] = key1
                # if label_analysis_param_tmp2 not in label_analysis_param_list:
                label_analysis_param_list.append(label_analysis_param_tmp2)
                for value3 in value2:
                    label_analysis_param_tmp3 = copy.copy(label_analysis_param_tmp2)
                    label_analysis_param_tmp3["segment"] = value3
                    # if label_analysis_param_tmp3 not in label_analysis_param_list:
                    label_analysis_param_list.append(label_analysis_param_tmp3)


    # print "label_analysis_param_list.len:", len(label_analysis_param_list)
    # print label_analysis_param_list

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


    label_Analysis_scale_cond = get_label_Analysis_cond(label_analysis_param_list, label_Analysis_scale)
    # label_Analysis_buyFeature_cond = get_label_Analysis_cond(label_analysis_param_list, label_Analysis_buyFeature)
    # label_Analysis_productLevel_cond = get_label_Analysis_cond(label_analysis_param_list, label_Analysis_productLevel)
    # label_Analysis_ChannelPrefer_cond = get_label_Analysis_cond(label_analysis_param_list, label_Analysis_ChannelPrefer)
    # label_Analysis_TimePrefer_cond = get_label_Analysis_cond(label_analysis_param_list, label_Analysis_TimePrefer)
    # label_Analysis_Groups_cond = get_label_Analysis_cond(label_analysis_param_list, label_Analysis_Groups)
    # label_Analysis_userValues_cond = get_label_Analysis_cond(label_analysis_param_list, label_Analysis_userValues)
    # label_Analysis_NetFeature_cond = get_label_Analysis_cond(label_analysis_param_list, label_Analysis_NetFeature)
    # label_Analysis_userNeed_cond = get_label_Analysis_cond(label_analysis_param_list, label_Analysis_userNeed)

    # 装箱所有请求url和参数
    request_url_all = [
        home_area_data,
        overview,
        buy_analytics,
        install_analytics,
        upkeep_analytics,
        service_analytics,
        consult_analytics,
        complaints_analytics,
        label_Analysis_tag_cloud,
        label_Analysis_scale,
        label_Analysis_buyFeature,
        label_Analysis_productLevel,
        label_Analysis_ChannelPrefer,
        label_Analysis_TimePrefer,
        label_Analysis_Groups,
        label_Analysis_userValues,
        label_Analysis_NetFeature,
        label_Analysis_userNeed,
        user_values_loyalty,
        user_values_value_search,
        user_search_searchUser,
        label_Analysis_targetUser,
        potential_users_search,

        label_Analysis_scale_cond,

        # 禁用以下cache
        # label_Analysis_buyFeature_cond,
        # label_Analysis_productLevel_cond,
        # label_Analysis_ChannelPrefer_cond,
        # label_Analysis_TimePrefer_cond,
        # label_Analysis_Groups_cond,
        # label_Analysis_userValues_cond,
        # label_Analysis_NetFeature_cond,
        # label_Analysis_userNeed_cond
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
print "开始发起[标签分析]cache请求..."
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

print "cache[标签分析]请求结束. 共发送[", reqCont, "]个请求. 耗时:", (datetime.datetime.now() - start_time).seconds, "秒"
