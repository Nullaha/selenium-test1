import os
from bs4 import BeautifulSoup
import requests
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import selenium.webdriver.support.ui as ui
import re
import docx

driver = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
driver.get("http://www.china-data-online.com/CensusMaps/RequestSearch")
driver.maximize_window()  # 浏览器最大化

driver.find_element_by_id("upperLevel1").click()
    # id="su"是百度搜索按钮，click() 是模拟点击
wait01 = ui.WebDriverWait(driver, 20)

driver.find_element_by_xpath("//*[@id='trIndex']/ul/li[3]/span/span[2]").click()
wait02 = ui.WebDriverWait(driver, 20)

#aha = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22']
ahaa = list(range(1, 16))
ahaaa = [str(i) for i in ahaa]
#for i in aha:
root1 = "//*[@id='trIndex']/ul/li[3]/ul/li["
root2 ="]/span/span[2]"
driver.find_element_by_xpath(root1+'3'+root2).click()
wait03 = ui.WebDriverWait(driver, 20)
n = 0
for j in ahaaa:
    root3 = "//*[@id='trIndex']/ul/li[3]/ul/li[3]/ul/li["
    root4 = "]/span/span[2]"
    driver.find_element_by_xpath(root3+j+root4).click()
    wait04 = ui.WebDriverWait(driver, 20)

    link = driver.find_element_by_css_selector(" div:nth-child(1)>div.item_content>div.item_name>a").get_attribute('href')
    print(link)
    n = n + 1
    wait05 = ui.WebDriverWait(driver, 20)
    time.sleep(3)
print(n)