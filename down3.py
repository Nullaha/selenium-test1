import os
import requests
import time
from selenium import webdriver
import selenium.webdriver.support.ui as ui
import re
import docx

sites = []
file = open("D:\Documents\Desktop\采矿业2.txt","r")


for para in file:
    para = para.strip('\n')
    sites.append(para)
    print(sites)

for site in sites:
    driver = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
    driver.get(site)
    driver.maximize_window()  # 浏览器最大化
    time.sleep(2)

    #driver.find_element_by_css_selector("div.exportControls > div:nth-child(2) > a").click()
    #wait02 = ui.WebDriverWait(driver, 20)
