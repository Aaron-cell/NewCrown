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

def insert_histery(data):
    """
    根据传入的data列表 循环插入表中
    :param data: 数据列表 封装的是字典
    :return:
    """
    cursor = None
    conn = None
    try:
        conn,cursor = getConnect()
        print(f"{time.asctime()}开始插入历史数据")
        sql = "insert into history values (%s,%s,%s,%s,%s,%s,%s,%s)"
        for dict in data:
            cursor.execute(sql,[dict['ds'],dict['confirm'],dict['confirm_add'],
                                dict['suspect'], dict['heal'],dict['heal_add'],
                                dict['dead'],dict['dead_add']])
        conn.commit()
        print(f"{time.asctime()}插入历史数据完毕")
    except:
        traceback.print_exc()
    finally:
        closeConnect(conn,cursor)
