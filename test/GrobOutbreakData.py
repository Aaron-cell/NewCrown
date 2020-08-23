import requests
import json
from bs4 import BeautifulSoup
#腾讯疫情官网
url = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5&callback=jQuery34108918489440097725_1598081532955&_=1598081532956'
header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0'}
res = requests.get(url,headers=header)
res.encoding = 'utf-8'
html = res.text
# soup = BeautifulSoup(html,'lxml')
# a = soup.find('a')
# print(a)
# print(a.attrs['href'])
#除去无效的数据
jsonData = html.replace('jQuery34108918489440097725_1598081532955(','')[:-1]
jsonData = json.loads(jsonData)
data = json.loads(jsonData['data'])
# print(data.keys())
print('lastUpdateTime:',data['lastUpdateTime'])
print('chinaTotal:',data['chinaTotal'])
print('chinaAdd:',data['chinaAdd'])
print('isShowAdd:',data['isShowAdd'])
print('showAddSwitch:',data['showAddSwitch'])
print('areaTree:',data['areaTree'])
# print(len(data['areaTree']))
# print(data['areaTree'][0])