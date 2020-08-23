import os
from config.Properties import Properties

# #当前文件夹位置
# curFolderPath = os.path.abspath(os.path.dirname(__file__))
# print(curFolderPath) #F:\MyCode\NewCrown\test
# #\\防止\被转译
# curFolderPath = str(curFolderPath).replace("\\","/")
# #配置文件路径
# mysqlConfigPath = curFolderPath+r'/MysqlConfig.properties'
# print(mysqlConfigPath)


#测试读取Mysql配置文件
properties = Properties().getProperties()
print(properties['host']) #localhost