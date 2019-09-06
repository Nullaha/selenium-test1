import sys
from bs4 import BeautifulSoup
import requests
import lxml
import re
import urllib.request
import time
import docx
from PyQt5.QtWebKits import *
from HTMLParser import HTMLParser
from PyQt5.QtGui import *
from PyQt5.QtCore import *


#第一步 从txt中获取核心code
sites = []
sites_code = []
file = open("D:\Documents\Desktop\经济普查\电力燃气.txt","r")

for para in file:
    para = para.strip('\n')
    sites.append(para)
print(sites)

for i in sites:
    ii = i.split('China/')
    sites_code.append(ii[-1])
print(sites_code)
print('code总数：'+str(len(sites_code)))


r = requests.session()

proxy_dict = {
    "http":"http://shenyue9586@stu:shenyue86@vpn,xjtu.edu.cn/",
    "https":"http://shenyue9586@stu:shenyue86@vpn,xjtu.edu.cn/"
}

def Schedule(blocknum,blocksize,totalsize):
    per = 100.0 * blocknum * blocksize / totalsize
    if per > 100:
        per = 100
    print('当前下载进度: %d'%per)

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36',
            'Cookie': 'JSESSIONID=5890C0C9820E0F27AA2ACCC5F1C5D371',
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
#image_urls = 'http://www.china-data-online.com/CensusMaps/RequestExport?exportType=png&mapID=8620082totalunits_08_1011&imagePath=cache/widget/staticMap/91d4fb781d8a5395a4fa7fe3e5a7c961af227ad4f90945b53ce428a378838138ded4152d3d473a4d4e46919a80b3bae4cd3dd1cbb4672e11d396a2f8ef675&mapTitle='


image_urls = []
urls = []
for i in sites_code:
    url2 = "http://www.china-data-online.com/CensusMaps/RequestExport?exportType=png&mapID={code}&imagePath=cache/widget/staticMap/91d4fb781d8a5395a4fa7fe3e5a7c961af227ad4f90945b53ce428a378838138ded4152d3d473a4d4e46919a80b3bae4cd3dd1cbb4672e11d396a2f8ef675&mapTitle=".format(code =i)
    url = "http://www.china-data-online.com/CensusMaps/map/China/{code}".format(code = i)
    image_urls.append(url2)
    urls.append(url)
print('图片地址为：')
print(image_urls)
#print('提取标题地址为：')
#print(urls)


class Render(QWebPage):
    def __init__(self,url):
        self.app = QApplication(sys.argv)
        QWebPage.__init__(self)
        self.loadFinished.connect(self._loadFinished)
        self.mainFrame().load(QUrl(url))
        self.app.exec_()
    def _loadFinished(self, result):
        self.frame = self.mainFrame()
        self.app.quit()



name1s = []
code2s = []
i=1
for url in urls:
    #web_data = r.get(url, headers=headers)
    #soup = BeautifulSoup(web_data.text, 'lxml')
    #print(soup)
    r = Render(url)
    html = r.frame.toHtml()
    print(html)


'''
    name1 = soup.select(' div.item_name_view > span')[0].text
    ha = name1 + str(i)
    print(ha)
    time.sleep(3)
    code2 = soup.select('div.widget_wrap > div.widget_map_center img')[0].get('src')
    #code3 ='http://www.china-data-online.com/CensusMaps/RequestExport?exportType=png&mapID='+ sites_code[i-1]+'&imagePath='+code2+'&mapTitle='
    print(code2)
    name1s.append(ha)
    code2s.append(code2)
    #time.sleep(1)
    i = i + 1
print(name1s)
print(code2s)


j = 0
for image_url in image_urls:

    web_data = r.get(image_url,headers=headers)
    time.sleep(3)
    #soup = BeautifulSoup(web_data.text,'lxml')
    #print(soup)
    local = 'D://Documents/Desktop/dianliranqi/'


    f = open(local +name1s[j]+'.png','wb')
    f.write(web_data.content)
    time.sleep(3)
    j = j + 1
'''
