#获取项目根路径
import os
import platform

def getRoot_Path():
    """
    对当前运行的系统判断，得到相应正确的项目根路径
    :return:
    """
    system = platform.system()
    curPath = os.path.abspath(os.path.dirname(__file__))
    if system == 'Windows':
        rootPath = curPath[:curPath.find("NewCrown\\")+len("NewCrown\\")]  # 获取myProject，也就是项目的根路径
        rootPath = str(rootPath).replace('\\','/')#路径\换成/   windows环境下
    elif system == 'Linux':
        rootPath = curPath[:curPath.find("NewCrown/")+len("NewCrown/")] #Linux环境下
    else:
        print('当前系统类型无法识别')
    print(rootPath)
    return rootPath

if __name__ == '__main__':
    rootPath = getRoot_Path()
    print(rootPath)

