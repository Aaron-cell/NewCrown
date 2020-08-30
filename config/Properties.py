from utils.RootPath import getRoot_Path
#读取Properties 文件类  配置文件路径config/MysqlConfig.properties
class Properties:
    #配置文件路径
    mysqlConfigPath = ''
    def __init__(self):
        #项目根路径
        root_Path = getRoot_Path()
        self.mysqlConfigPath = root_Path+r'/config/MysqlConfig.properties'

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
