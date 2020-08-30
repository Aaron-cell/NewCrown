from flask import Flask
from flask import request

app = Flask(__name__)
# 测试简单使用flask轻量级web框架
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