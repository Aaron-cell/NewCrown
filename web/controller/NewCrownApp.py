from flask import Flask,jsonify
from flask import render_template
from utils.RootPath import getRoot_Path
import time
from web.Service import HistoryService as historyService,DetailsService as detailsService


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

if __name__ == '__main__':
    #host='0.0.0.0'可被外网访问 port指定端口号 debug= true 开启debug模式
    app.run(host = '127.0.0.1',port='8080',debug=True)