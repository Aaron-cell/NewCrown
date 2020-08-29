import pymysql as jdbc # 导入mysql连接包
import time
from config.Properties import Properties
import traceback


#获取数据库连接
def getConnect():
    #测试读取Mysql配置文件
    properties = Properties().getProperties()
    conn = jdbc.connect(host=properties['host'],port=int(properties['port']),user=properties['user'],password=properties['password'],db=properties['database'],charset ='utf8')
    #创建游标 游标概念 游标对象用于执行、查询和获取结果。 一条sql，对应N条资源，取出资源的接口，就是游标，沿着游标，可以一次取出1行。
    cursor = conn.cursor()
    return conn,cursor

#关闭连接
def closeConnect(conn, cursor):
    if cursor:
        cursor.close()
    if conn:
        conn.close()


def query(sql,*args):
    """ 查询
    :param sql:
    :param args:
    :return:
    """
    conn,cursor = getConnect()
    cursor.execute(sql,args)
    #通过游标 获取数据 结果集是元组类型
    res = cursor.fetchall()
    closeConnect(conn,cursor)
    return res

def insertHistery(dict):
    """
    根据传入的dict字典 循环插入表中
    :param data: 字典
    :return:
    """
    cursor = None
    conn = None
    try:
        conn,cursor = getConnect()
        sql = "insert into history values (%s,%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(sql,[dict['ds'],dict['confirm'],dict['confirm_add'],
                            dict['now_confirm'], dict['heal'],dict['heal_add'],
                            dict['dead'],dict['dead_add']])
        conn.commit()
    except:
        traceback.print_exc()
    finally:
        closeConnect(conn,cursor)

def getHistoryByDs(ds):
    """
    根据history表的主键（时间）获取数据
    :param ds:  时间
    :return: res 元组
    """
    try:
        sql = "select * from history where ds = \'"+ds+"\'"
        res = query(sql)
        return res
    except:
        traceback.print_exc()

def getDetailsByTime(update_time):
    """
    根据details表的字段（update_time）查询数据
    :param update_time:  时间
    :return: res 元组
    """
    try:
        sql = "select * from details where update_time = \'"+update_time+"\'"
        res = query(sql)
        return res
    except:
        traceback.print_exc()


def insertDetails(list):
    """
    根据传入的list列表 list中封装的是元组
    这里使用executemany 批量插入 多倍快乐
    :param data: 数据列表 封装的是元组
    :return:
    """
    cursor = None
    conn = None
    try:
        conn,cursor = getConnect()
        sql = "insert into details (update_time,province,city,confirm,confirm_add,heal,dead)" \
              "values (%s,%s,%s,%s,%s,%s,%s)"
        cursor.executemany(sql,list)
        conn.commit()
    except:
        traceback.print_exc()
    finally:
        closeConnect(conn,cursor)

def insertHotSearch(hotList):
    """
    根据传入的list列表 list中封装的是元组
    这里使用executemany 批量插入 多倍快乐
    :param data: 数据列表 封装的是元组
    :return:
    """
    cursor = None
    conn = None
    try:
        conn,cursor = getConnect()
        sql = "insert into hotsearch (dt,content)" \
              "values (%s,%s)"
        cursor.executemany(sql,hotList)
        conn.commit()
    except:
        traceback.print_exc()
    finally:
        closeConnect(conn,cursor)
