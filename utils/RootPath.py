#获取项目根路径
import os

def getRoot_Path():
    curPath = os.path.abspath(os.path.dirname(__file__))
    rootPath = curPath[:curPath.find("NewCrown\\")+len("NewCrown\\")]  # 获取myProject，也就是项目的根路径
    rootPath = str(rootPath).replace('\\','/')#路径\换成/
    return rootPath

