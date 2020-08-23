import os
#读取Properties 文件类  配置文件路径config/MysqlConfig.properties
class Properties:
    #配置文件路径
    mysqlConfigPath = ''
    def __init__(self):
        #当前文件夹位置
        curFolderPath = os.path.abspath(os.path.dirname(__file__))
        #\\防止\被转译
        curFolderPath = str(curFolderPath).replace("\\","/") #F:/MyCode/NewCrown/test
        self.mysqlConfigPath = curFolderPath+r'/MysqlConfig.properties'

    def getProperties(self):
        try:
            pro_file = open(self.mysqlConfigPath, 'r',encoding='utf8')
            properties = {} #定义一个字典
            for line in pro_file:
                if line.find('=') > 0:
                    strs = line.replace('\n', '').split('=')
                    properties[strs[0]] = strs[1]
        except Exception as e:
            raise e
        else:
            pro_file.close()
        return properties
