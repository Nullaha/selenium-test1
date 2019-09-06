from bs4 import BeautifulSoup
import requests
import lxml
import re
import urllib.request
import time
import docx

r = requests.session()

proxy_dict = {
    "http":"http://shenyue9586@stu:shenyue86@vpn,xjtu.edu.cn/",
    "https":"http://shenyue9586@stu:shenyue86@vpn,xjtu.edu.cn/"
}



headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36',
            'Cookie': 'JSESSIONID=3DE48B60BE51383CDEB605DE4621E3AD',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Upgrade-Insecure-Requests': '1',
            'Host': 'www.china-data-online.com',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.2 Safari/605.1.15',
            'Accept-Language': 'zh-cn',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive'}

#url = "http://www.china-data-online.com/CensusMaps/home"
#web_data = r.get(url,headers=headers)
#soup = BeautifulSoup(web_data.text,'lxml')
#print(soup)


#生成 png网址
image_urls = 'http://www.china-data-online.com/CensusMaps/RequestExport?exportType=png&mapID=8620082in_8110_08_1011&imagePath=b22d1ef1dccde4d59a7f6ccef245c33fbeaef92e87bbd6079c4f87f3c7f442a685de5115eb14f53b56cfcd429817a239782c782227a3f7243b6f0a8732f36f2&mapTitle='

web_data = r.get(image_urls,headers=headers)
#time.sleep(3)
soup = BeautifulSoup(web_data.text,'lxml')
print(soup)
local ='D://Documents/Desktop/'
f = open(local+'6.png','wb')
f.write(web_data.content)


#local = 'D://Documents/Desktop/images/'
#a='3.png'
#urllib.request.urlretrieve(image_urls,local+a,Schedule)
