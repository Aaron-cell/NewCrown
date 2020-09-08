from datasource.Sipder import getTencentData,getHotData,getHotSearchData
import utils.JdbcTemplet as jdbc
import sys
def insertHistory(data):
    """
    将抓取的数据解析 插入数据库
    :return:
    """
    #封装字典前 先判断当前数据是否在表中存在 存在则不插入
    ds = data['lastUpdateTime']
    res = jdbc.getHistoryByDs(ds)
    if len(res) >0 :
        return

    history={}
    history['ds']=ds
    history['confirm'] =data['chinaTotal']['confirm']
    history['confirm_add']=data['chinaAdd']['confirm'] #新增确诊
    history['now_confirm']=data['chinaTotal']['nowConfirm'] #现有确诊
    history['heal']=data['chinaTotal']['heal'] #累计治愈
    history['heal_add']=data['chinaAdd']['heal'] #新增治愈
    history['dead']=data['chinaTotal']['dead']
    history['dead_add']=data['chinaAdd']['dead']

    #插入数据库
    jdbc.insertHistery(history)
    pass

def insertDetails(data):
    """
    解析数据 将数据插入到details表中
    :param data: 数据源
    :return: list 一个列表 封装的是元组，每个元组便是一条数据
    """
    #封装列表前 先判断当前数据是否在表中存在 存在则不插入
    update_time = data['lastUpdateTime']
    res = jdbc.getDetailsByTime(update_time)
    if len(res) >0 :
        return

    details = [] #数据列表
    countryList = data['areaTree']#国家树形数据 一个列表
    for countryDict in countryList:
        provinceList = countryDict['children']
        for provinceDict in provinceList :
            province = provinceDict['name'] #省
            cityList = provinceDict['children'] #市 列表
            for cityDict in cityList :
                city = cityDict['name'] #市
                confirm = cityDict['total']['confirm'] #累计确诊
                confirm_add = cityDict['today']['confirm'] #新增确诊
                heal = cityDict['total']['heal']
                dead = cityDict['total']['dead']
                #封装元组 加入列表
                details.append((update_time,province,city,confirm,confirm_add,heal,dead))

    #插入数据
    print(details)
    jdbc.insertDetails(details)
    pass

def insertHotSearch(hotSearchList,dt):
    """
    解析从百度抓取的热点数据，然后插入到数据库
    :param hotList:
    :return:
    """
    #删除今日 热搜数据 在进行插入操作
    jdbc.delHotSearchData(dt)
    jdbc.insertHotSearch(hotSearchList)
    pass


if __name__ == "__main__":
    len = len(sys.argv)
    if len == 1:
        msg = """
            请输入一下参数:
            up_tencent 更新腾讯疫情数据
            up_baidu 更新百度热点数据
            """
        print(msg)
    else:
        arg = sys.argv[1]
        if arg == 'up_tencent':
            data = getTencentData()
            insertHistory(data)
            insertDetails(data)
        elif arg == 'up_baidu':
            hotSearchList, dt = getHotSearchData()
            insertHotSearch(hotSearchList, dt)
        else:
            msg = '无效参数，请仔细检查！'
            print(msg)

