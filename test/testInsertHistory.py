import utils.jdbcTemplet as jdbc
import time
import random

#获取当前时间
#定义一个列表 一个字典
list =[]

t = time.localtime(time.time())
t1 = time.strftime('%Y-%m-%d %H:%M:%S',t)
dict ={}
dict['ds']=t1
dict['confirm'] =1
dict['confirm_add']=1
dict['suspect']=1
dict['heal']=1
dict['heal_add']=1
dict['dead']=1
dict['dead_add']=1
list.append(dict)
jdbc.insert_histery(list)