import requests
import json

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
