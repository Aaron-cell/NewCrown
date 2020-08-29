import requests
import json
from bs4 import BeautifulSoup
from selenium.webdriver import Chrome,ChromeOptions
#百度疫情官网
url = 'https://voice.baidu.com/act/virussearch/virussearch?from=osari_map&tab=0&infomore=1'
header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0'}
res = requests.get(url,headers=header)
res.encoding = 'utf-8'
html = res.text
# soup = BeautifulSoup(html,'lxml')
# a = soup.find('a')
# print(a)
# print(a.attrs['href'])
#除去无效的数据
# jsonData = html.replace('jQuery34108918489440097725_1598081532955(','')[:-1]
# jsonData = json.loads(jsonData)
# data = json.loads(jsonData['data'])
# print(data.keys())
# print('lastUpdateTime:',data['lastUpdateTime'])
# print('chinaTotal:',data['chinaTotal'])
# print('chinaAdd:',data['chinaAdd'])
# print('isShowAdd:',data['isShowAdd'])
# print('showAddSwitch:',data['showAddSwitch'])
# print('areaTree:',data['areaTree'])
# print(len(data['areaTree']))
# print(data['areaTree'][0])

print(html)