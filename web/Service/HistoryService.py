from utils import JdbcTemplet as jdbc

def getLastHistory():
    sql ='select confirm,now_confirm,heal,dead from history ORDER BY ds DESC LIMIT 1'
    res = jdbc.query(sql)
    print(res[0])
    return res[0]

if __name__ == '__main__':
    getLastHistory()
