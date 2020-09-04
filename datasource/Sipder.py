import requests
import json
from selenium.webdriver import Chrome,ChromeOptions
import time
from utils.RootPath import getRoot_Path

def getTencentData():
    #腾讯疫情抓取资源请求url
    url = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5&callback=jQuery34108918489440097725_1598081532955&_=1598081532956'
    header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0'}
    res = requests.get(url,headers=header)
    res.encoding = 'utf-8'
    jsonData = res.text
    #除去无效的数据
    jsonData = jsonData.replace('jQuery34108918489440097725_1598081532955(','')[:-1]
    jsonData = json.loads(jsonData)
    data = json.loads(jsonData['data']) #返回有效数据
    return data
#已停用
def getHotData():
    """
    抓取百度 关于疫情的热点数据
    :return:
    """
    #项目根路径 用于指定谷歌插件的路径
    root_Path = getRoot_Path()
    #隐藏游览器
    option = ChromeOptions()
    option.add_argument("--headless")
    option.add_argument("--no--sandbox") #b部署到linux时需要设置 无插盘模式
    browser = Chrome(options=option,executable_path= root_Path+'/plugin/chromedriver.exe')
    url = "https://voice.baidu.com/act/virussearch/virussearch?from=osari_map&tab=0&infomore=1"
    browser.get(url)
    #打印获取的数据
    # print(browser.page_source)
    #获取查看更多按钮 selector 或xpath都能获取到
    # button = browser.find_element_by_css_selector('#ptab-0 > div > div.VirusHot_1-5-6_32AY4F.VirusHot_1-5-6_2RnRvg > section > div')
    # button.click() #模拟点击
    # time.sleep(1) #模拟人点击 等待一秒
    hotArray = browser.find_elements_by_xpath('//*[@id="area"]/div[2]/section/a/div/span[2]')
    #打印获取内容
    hotList =[]
    for hotData in hotArray:
        hotList.append(hotData.text)
        print(hotData.text)
    browser.close()
    return hotList

def getHotSearchData():
    """
    抓取百度 热搜数据
    :return:
    """
    #项目根路径 用于指定谷歌插件的路径
    root_Path = getRoot_Path()
    #隐藏游览器
    option = ChromeOptions()
    option.add_argument("--headless")
    option.add_argument("--no--sandbox") #b部署到linux时需要设置 无插盘模式
    browser = Chrome(options=option,executable_path= root_Path+'/plugin/chromedriver.exe')
    url = "http://top.baidu.com/buzz?b=341&fr=topbuzz_b1_c513"
    browser.get(url)
    hotArray = browser.find_elements_by_xpath('//*[@id="main"]/div[2]/div/table/tbody/tr/td')
    #打印获取内容
    hotSearchList =[]
    #hotArray size = 200
    dt = time.strftime("%Y-%m-%d")
    for i in range(1,199,4):
        hotSearchContent = hotArray[i].text
        hotSearchNumber = hotArray[i+2].text
        hotSearchList.append((dt,hotSearchContent,hotSearchNumber))
    browser.close()
    return hotSearchList,dt



if __name__ == '__main__':
    # 测试
    getHotSearchData()



