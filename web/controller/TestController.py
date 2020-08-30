from flask import Flask
from flask import request
from flask import render_template
from utils.RootPath import getRoot_Path


root_Path = getRoot_Path()
# 创建flask的应用对象
# __name__表示当前模块的名字
# 参数__name__表示flask以哪个模块所在目录当做项目的根目录，项目根目录中默认static为静态目录，templates为模板目录
app = Flask(__name__,
            static_url_path="/static",  # 访问静态资源的url前缀, 默认值是static
            static_folder=root_Path+"/static",  # 静态文件的存放目录，默认就是static
            template_folder=root_Path+"/templates",  # 模板文件的目录，默认是templates
            )
# 测试简单使用flask轻量级web框架
@app.route('/')
def index():
    return render_template('main.html')

@app.route('/hello')
def sayHello():
    return 'hello,world'

@app.route('/test',methods=['get','post'])
def test():
    id = request.values.get("id") #获取请求参数
    print(id)
    return f"""
    <form action="/login" method="post">
            账号：<input name="name" value="{id}"><br>
            密码：<input name="pwd"> 
            <input type="submit">
        </form>
    """

@app.route('/login',methods=['post'])
def login():
    name = request.values.get("name")
    pwd = request.values.get("pwd")
    return f'name={name}.pwd={pwd}'

if __name__ == '__main__':

    app.run(host = '127.0.0.1',port='8080')