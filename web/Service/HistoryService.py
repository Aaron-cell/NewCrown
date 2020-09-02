from utils import JdbcTemplet as jdbc

def getLastHistory():
    """
    查询最新的一条历史数据
    :return:
    """
    sql ='select confirm,now_confirm,heal,dead from history ORDER BY ds DESC LIMIT 1'
    res = jdbc.query(sql)
    return res[0]

def getAllHistory():
    """
    查询所有历史记录 展示ds,confirm,now_confirm,heal,dead
    :return:
    """
    sql='select ds,confirm,now_confirm,heal,dead from history'
    res = jdbc.query(sql)
    return res

def getAddHistory():
    """
    查询所有历史记录 展示ds,confirm_add，heal_add，dead_add
    :return:
    """
    sql='select ds,confirm_add,heal_add,dead_add from history'
    res = jdbc.query(sql)
    return res

if __name__ == '__main__':
    getLastHistory()
