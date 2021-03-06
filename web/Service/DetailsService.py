from utils import JdbcTemplet as jdbc

def getLastDetails():
    """
    查询最新时间 各个省的疫情累计情况
    :return:
    """
    sql ='select province,SUM(confirm) as confirm,SUM(confirm_add) as confirm_add,' \
         'SUM(heal) as heal,SUM(dead) as dead from details ' \
         'where update_time =(select update_time from details  GROUP BY update_time ORDER BY update_time DESC LIMIT 1) ' \
         'GROUP BY province '
    res = jdbc.query(sql)
    return res

def getLastConfirm():
    """
    查询全国累计确诊非湖北前五的城市
    :return:
    """
    sql ='select province,SUM(confirm) as confirm from details ' \
         'where province != "湖北" ' \
         'and update_time =(select update_time from details  GROUP BY update_time ORDER BY update_time DESC LIMIT 1) ' \
         'GROUP BY province ' \
         'ORDER BY confirm DESC LIMIT 5'
    res = jdbc.query(sql)
    return res

if __name__ == '__main__':
    getLastDetails()