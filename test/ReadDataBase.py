import utils.jdbcTemplet as jdbc
sql ='select * from history'
res = jdbc.query(sql)
#res 是 tuple类型
for tup in res:
    print(tup)