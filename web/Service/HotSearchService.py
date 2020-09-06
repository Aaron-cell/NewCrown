from utils.JdbcTemplet import query

def getToDayHotData(dt):
    """
    获取今天排名前20的热搜数据
    :param dt:
    :return:
    """
    sql = 'select content,search_num from hotsearch where dt =\''+dt+'\' ORDER BY search_num desc LIMIT 20'
    res = query(sql=sql)
    return res