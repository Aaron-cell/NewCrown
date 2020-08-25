from datasource.Sipder import getTencentData
import utils.JdbcTemplet as jdbc

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

if __name__ == "__main__":
    #测试 好不好用
    data = getTencentData()
    insertHistory(data)

