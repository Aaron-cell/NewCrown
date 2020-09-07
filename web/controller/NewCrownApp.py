import os
import sys
import platform
# 将项目根路径设置为环境变量
system = platform.system()
curPath = os.path.abspath(os.path.dirname(__file__))
if system == 'Windows':
    rootPath = curPath[:curPath.find("NewCrown\\")+len("NewCrown\\")]  # 获取myProject，也就是项目的根路径
    rootPath = str(rootPath).replace('\\','/')#路径\换成/   windows环境下
elif system == 'Linux':
    rootPath = curPath[:curPath.find("NewCrown/")+len("NewCrown/")] #Linux环境下
else:
    print('当前系统类型无法识别')
sys.path.append(rootPath) #将项目所在路径加入python模块搜索路径
from flask import Flask,jsonify
from flask import render_template
import time
from jieba.analyse import extract_tags
from utils.RootPath import getRoot_Path
from web.Service import HistoryService as historyService,\
    DetailsService as detailsService,HotSearchService as hotSearchService


root_Path = getRoot_Path()
# 创建flask的应用对象
# __name__表示当前模块的名字
# 参数__name__表示flask以哪个模块所在目录当做项目的根目录，项目根目录中默认static为静态目录，templates为模板目录
app = Flask(__name__,
            static_url_path="/static",  # 访问静态资源的url前缀, 默认值是static
            static_folder=root_Path+"/static",  # 静态文件的存放目录，默认就是static
            template_folder=root_Path+"/templates",  # 模板文件的目录，默认是templates
            )

@app.route('/')
def index():
    """
    项目欢迎页
    :return:
    """
    return render_template('main.html')

@app.route('/newcrown/time',methods=['get'])
def nowTime():
    """
    页面上刷新的时间
    :return:
    """
    time_str = time.strftime("%Y{}%m{}%d{} %X")
    return time_str.format("年","月","日")

@app.route('/newcrown/history',methods=['get'])
def getHistoryData():
    """
    展示首页累计确诊，现有确诊，累计治愈，累计死亡数据
    jsonify：将字典转换为json
    :return:
    """
    lastData = historyService.getLastHistory()
    return jsonify({'confirm':lastData[0],'now_confirm':lastData[1],'heal':lastData[2],'dead':lastData[3]})

@app.route('/newcrown/c2',methods=['get'])
def getDetailsData():
    """
    展示首页中国地图中疫情数据
    :return:
    """
    resList =[]
    lastDetailsData = detailsService.getLastDetails()
    for res in lastDetailsData:
        resList.append({'name':res[0],'value':int(res[1])})
    return jsonify({'data':resList})

@app.route('/newcrown/l1',methods=['get'])
def getAllHistory():
    """
    显示全国累计趋势折线图
    :return:
    """
    res = historyService.getAllHistory()
    day,confirm,now_confirm,heal,dead = [],[],[],[],[]
    for a,b,c,d,e in res:
        day.append(a.strftime("%m-%d"))
        confirm.append(b)
        now_confirm.append(c)
        heal.append(d)
        dead.append(e)
    return jsonify({"day":day,"confirm":confirm,"now_confirm":now_confirm,"heal":heal,"dead":dead})

@app.route('/newcrown/l2',methods=['get'])
def getAddHistory():
    """
    显示全国新增趋势折线图
    :return:
    """
    res = historyService.getAddHistory()
    day,confirm_add,heal_add,dead_add = [],[],[],[]
    for a,b,c,d in res:
        day.append(a.strftime("%m-%d"))
        confirm_add.append(b)
        heal_add.append(c)
        dead_add.append(d)
    return jsonify({"day":day,"confirm_add":confirm_add,"heal_add":heal_add,"dead_add":dead_add})

@app.route('/newcrown/r1',methods=['get'])
def getTop5City():
    """
    获取国内疫情累计确诊人数前五的城市
    :return:
    """
    res = detailsService.getLastConfirm();
    province,confirm =[],[]
    for a,b in res:
        province.append(a)
        confirm.append(int(b))
    return jsonify({"province":province,"confirm":confirm})

@app.route('/newcrown/r2',methods=['get'])
def getToDayHotSearch():
    """
    查询当前日期 热搜指数前20条数据
    :return:
    """
    dt = time.strftime("%Y-%m-%d")
    res = hotSearchService.getToDayHotData(dt)
    keyWordsCloud=[] #词云列表
    for content,search_num in res:
        #sentence 分词内容，topK关键字字数，允许提取的词性 返回的是一个关键词列表
        #博客 https://blog.csdn.net/qq_38101190/article/details/90750188
        keyWords = extract_tags(sentence=content,topK=4,allowPOS=('ns','n','vn','v'))
        for kw in keyWords:
            if not kw.isdigit():
                keyWordsCloud.append({"name": kw,"value": search_num})

    return jsonify({"keyWordsCloud":keyWordsCloud})


if __name__ == '__main__':
    #host='0.0.0.0'可被外网访问 port指定端口号 debug= true 开启debug模式
    app.run(host = '0.0.0.0',port='8080',debug=False)