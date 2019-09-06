from bs4 import BeautifulSoup
import requests
import lxml
import os
import re
import urllib.request
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import selenium.webdriver.support.ui as ui
import docx

#os.makedirs('./img/',exist_ok=True)

#第一步 从txt中获取核心code
sites = []
sites_code = []
file = open("D:\Documents\Desktop\采矿业.txt","r")

for para in file:
    para = para.strip('\n')
    sites.append(para)
print(sites)

for i in sites:
    ii = i.split('China/')
    sites_code.append(ii[-1])
print(sites_code)
print('code总数：'+str(len(sites_code)))


#生成 png网址
ex_urls = []
urls = []
for i in sites_code:
    url2 = "http://www.china-data-online.com/CensusMaps/RequestExport?exportType=xls&mapID={code}&imagePath=cache/widget/staticMap/91d4fb781d8a5395a4fa7fe3e5a7c961af227ad4f90945b53ce428a378838138ded4152d3d473a4d4e46919a80b3bae4cd3dd1cbb4672e11d396a2f8ef675&mapTitle=".format(code =i)
    #url = "http://www.china-data-online.com/CensusMaps/map/China/{code}".format(code = i)
    ex_urls.append(url2)
    #urls.append(url)
print('图片地址为：')
print(ex_urls)
#print('提取标题地址为：')
#print(urls)


file = docx.Document()
for word in ex_urls:
    file.add_paragraph(word)

file.save("D:\Documents\Desktop\writeResult.docx")






'''
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'}
cookies = {'JSESSIONID': '841EA58EF8486269D31824C4C0EC5561'}
urla = "http://www.china-data-online.com/CensusMaps/home"
web_data = requests.get(urla,headers=headers,cookies=cookies)
soup = BeautifulSoup(web_data.text,'lxml')


name = []
for url in urls:
    web_data = requests.get(url, headers=headers, cookies=cookies)
    soup = BeautifulSoup(web_data.text, 'lxml')
    haha = soup.select(' div.item_name_view > span')
    name.append(haha)
print(name)


def Schedule(blocknum,blocksize,totalsize):
    per = 100.0 * blocknum * blocksize / totalsize
    if per > 100:
        per = 100
    print('当前下载进度: %d'%per)





local = 'D://Documents/Desktop/images/'
hh = ['a','b','c']
i = 0
for image in image_urls:
    web_data = requests.get(image, headers=headers, cookies=cookies)
    soup = BeautifulSoup(web_data.text, 'lxml')
    urllib.request.urlretrieve(image,local+hh[i],Schedule)
    i = i+1

'''