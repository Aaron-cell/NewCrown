# NewCrown
### 全国疫情实时追踪
#### 1.技术

+ 语言：python
+ 前端：jquery、echarts
+ 后端：Flask轻量级web框架
+ 数据源：selenium、request模块
+ 数据存储：mysql
+ 代理服务器：Nginx

#### 2.数据源
+ 项目中全国疫情数据来自腾讯疫情，热搜数据来自百度疫情热搜
    + 腾讯疫情：https://news.qq.com/zt2020/page/feiyan.htm#/?pool=hb&nojump=1
    + 百度疫情热搜：http://top.baidu.com/buzz?b=341&fr=topbuzz_b1_c513
 
#### 3.项目部署
+ 项目部署遇到的问题
    + 1.直接运行newCrownApp文件，出现根据相对路径导入模块失败的问题，在导包是将项目根路径加入到python导入模块搜索路径
    
+ 将项目运行的WSGI服务器是Gunicorn，并通过Nginx进行反向代理
    + 开启守护进程命令：gunicorn -b 127.0.0.1:8080 -D NewCrownApp:app
    + Nginx使用命令：https://www.jianshu.com/p/48bd46fb891d
+ 项目访问链接 http://119.45.228.191/

