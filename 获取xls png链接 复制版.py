import os
from selenium import webdriver
import selenium.webdriver.support.ui as ui
import re
from bs4 import BeautifulSoup
import requests
import lxml
import urllib.request
import time



sites = [] #如http://www.china-data-online.com/CensusMaps/map/China/8620082in_4610_08_1014
sites_code = []  #如8620082in_4610_08_1014

# 更改链接txt处！！！！
file = open("D:\\Documents\Desktop\经济普查\房地产业14.txt","r")

for para in file:
    sites.append(para)
    print(para)

for i in sites:
    i = i.strip('\n')
    ii = i.split('China/')
    sites_code.append(ii[-1])
print(sites_code)
print('code总数：'+str(len(sites_code)))

r = requests.session()

proxy_dict = {
    "http":"http://shenyue9586@stu:shenyue86@vpn,xjtu.edu.cn/",
    "https":"http://shenyue9586@stu:shenyue86@vpn,xjtu.edu.cn/"
}


headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36',
            'Cookie': 'JSESSIONID=040A09FA1C97B61D7EFC40FA1563D915',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Upgrade-Insecure-Requests': '1',
            'Host': 'www.china-data-online.com',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.2 Safari/605.1.15',
            'Accept-Language': 'zh-cn',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive'}



titles = []
image_codes = [] #如http://www.china-data-online.com/CensusMaps/cache/widget/staticMap/3d7de468dffdbf7ed558f8ae2458fb3837c48c5678dfc268fc66899b768016383af9ef4d95a91e74e629d9d3f98b7244099980adcf47e9bcd5b4bef4277c
j = 0
for site in sites:
    driver = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
    driver.get(site)
    time.sleep(3)


    #获取title
    titlea = driver.find_element_by_css_selector("div.item_name_view > span").get_attribute('textContent')
    title = titlea + str(j)
    print(title)
    titles.append(title)


    #获取image地址
    image = driver.find_element_by_css_selector(" div > div.widget_wrap > div.widget_map_center img").get_attribute(
        'src')
    ii = image.split('staticMap/')
    #print(ii[-1])
    iii ='http://www.china-data-online.com/CensusMaps/RequestExport?exportType=png&mapID='+ sites_code[j]+'&imagePath='+ii[-1]+'&mapTitle='
    print(iii)
    image_codes.append(iii)

    #下载png
    web_data = r.get(iii,headers=headers)
    #time.sleep(1)

    #更改images保存处！！！！！
    local = 'D://Documents/Desktop/images/房地产业14/'
    f = open(local +title+'.png','wb')
    f.write(web_data.content)
    time.sleep(2)


    #点击xls下载
    driver.find_element_by_css_selector("div.exportControls > div:nth-child(2) > a").click()
    wait02 = ui.WebDriverWait(driver, 20)
    j = j +1




