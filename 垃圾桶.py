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

# 第一步
zuozhe = []
titles = []


def file_name(file_dir):
    find_files = []
    n = 0
    for root, dirs, files in os.walk(file_dir):
        for i in files:
            n = n + 1
            # print('root_dir:', root)
            # print('sub_dirs:', dirs)
            # print('files:', files)
            find_files.append(i)
    print('find_files:', find_files)  # 打印所有files
    print(n)

    find_files2 = list(set(find_files))  # 删除重复

    print('find_files2:', find_files2)  # 打印没有重复的files
    print(len(find_files2))

    # 筛选pdf和caj并去掉后缀
    find_files3 = []
    for i in find_files2:
        if '.pdf' in i or '.caj' in i:
            ii = i.split('.')
            find_files3.append(ii[0])
    print('find_files3', find_files3)  # 打印pdf或caj格式的files
    print(len(find_files3))

    # 按_分离名字

    for j in find_files3:
        jj = j.split('_')
        jjj = ''.join(jj[:-1])
        zuozhe.append(jj[-1])

        titles.append(jjj)
    print(zuozhe)
    print(titles)


file_name('D:\Documents\Desktop\乡村振兴')

zuhe = dict(zip(titles, zuozhe))
print(zuhe)

# 第二步
driver = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
driver.get("http://kns.cnki.net/kns/brief/result.aspx?dbprefix=SCDB")
driver.maximize_window()  # 浏览器最大化

wangzhi = []
wxwangzhi = []
for key, value in zuhe.items():
    # id=".."是搜索框，输入字符串“..”，跳转到搜索中国页面
    driver.find_element_by_id("txt_1_value1").send_keys(key)
    wait02 = ui.WebDriverWait(driver, 20)
    driver.find_element_by_id("au_1_value1").send_keys(value)
    driver.find_element_by_id("au_1_value1").click()
    # id="su"是百度搜索按钮，click() 是模拟点击
    wait01 = ui.WebDriverWait(driver, 20)

    sear = driver.find_element_by_xpath("//*[@id='btnSearch']")
    driver.execute_script("arguments[0].click()", sear)

    driver.execute_script("window.scrollTo(0, 300);")
    # h = document.body.scrollHeight
    wait = ui.WebDriverWait(driver, 20)
    # wait.until(lambda driver: driver.find_element_by_xpath("//*[@id='Form1']/div[4]/div[1]/div[2]/div[1]/a[1]"))
    # new_url = driver.find_element_by_xpath("//*[@id='Form1']/div[4]/div[1]/div[2]/div[1]/a[1]").get_attribute("href")

    driver.switch_to.frame("iframeResult")

    time.sleep(3)  # 决定成败的一击！！！

    # 点击网页1中的 参考文献超链接。
    new_url = driver.find_element_by_xpath("//*[@id='ctl00']/table/tbody/tr[2]/td/table/tbody/tr[2]/td[2]/a")
    driver.execute_script("arguments[0].click()", new_url)  # 用了js方法

    # 获取目前有的两个网页，并定位到第二个网页进行标题和网页二url的获取，并添加到wangzhi列表中。
    all_handles = driver.window_handles  # 获取所有窗口句柄
    # print(all_handles)
    driver.switch_to.window(all_handles[1])
    ceshi = driver.find_element_by_css_selector("#mainArea > div.wxmain > div.wxTitle > h2").get_attribute(
        'textContent')
    print(ceshi)
    url5 = driver.current_url
    print(url5)
    wangzhi.append(url5)  # 把网页2的网址添加到列表里。

    # 点击网页2中的 参考文献超链接。
    wenxianwz = driver.find_element_by_css_selector(
        "#mainArea > div.wxmain > div.wxTitle > div.link > a.icon.icon-output")
    driver.execute_script("arguments[0].click()", wenxianwz)  # 用了js方法

    # 获取目前有的三个网页，并定位到第三个网页进行参考文献text获取，并添加到wxwangzhi列表中。
    all_handles2 = driver.window_handles  # 获取目前所有窗口句柄
    driver.switch_to.window(all_handles2[2])
    url6 = driver.find_element_by_css_selector(
        "#main > table > tbody > tr:nth-child(2) > td > table > tbody > tr > td.detailMode > table > tbody > tr > td").get_attribute(
        'textContent')
    wxwangzhi.append(url6)

    # 关闭网页3 网页2
    wait3 = ui.WebDriverWait(driver, 20)
    driver.close()
    wait31 = ui.WebDriverWait(driver, 20)
    driver.switch_to.window(all_handles2[1])
    driver.close()

    wait4 = ui.WebDriverWait(driver, 20)
    driver.switch_to.window(all_handles[0])
    driver.execute_script("window.scrollTo(0, 0);")
    driver.refresh()  # 刷新页面
    time.sleep(2)
print(wangzhi)
print(wxwangzhi)

# 第五步
file = docx.Document()
for word in wxwangzhi:
    file.add_paragraph(word)

file.save("D:\Documents\Desktop\乡村振兴\writeResult.docx")