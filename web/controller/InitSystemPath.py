import os
import sys
import platform

# def initSystemPath():
#     # 将项目根路径设置为环境变量
#     system = platform.system()
#     curPath = os.path.abspath(os.path.dirname(__file__))
#     if system == 'Windows':
#         rootPath = curPath[:curPath.find("NewCrown\\")+len("NewCrown\\")]  # 获取myProject，也就是项目的根路径
#         rootPath = str(rootPath).replace('\\','/')#路径\换成/   windows环境下
#     elif system == 'Linux':
#         rootPath = curPath[:curPath.find("NewCrown/")+len("NewCrown/")] #Linux环境下
#     else:
#         print('当前系统类型无法识别')
#     sys.path.append(rootPath)
#     print("设置环境变量成功！")
#     print(sys.path)
#
# if __name__ !='__main__':
#     initSystemPath()