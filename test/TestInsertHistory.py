import utils.JdbcTemplet as jdbc
import time
import random

#获取当前时间
#一个字典
t = time.localtime(time.time())
t1 = time.strftime('%Y-%m-%d %H:%M:%S',t)
dict ={}
dict['ds']=t1
dict['confirm'] =1
dict['confirm_add']=1
dict['now_confirm']=1
dict['heal']=1
dict['heal_add']=1
dict['dead']=1
dict['dead_add']=1
jdbc.insertHistery(dict)