# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup as BS


import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait as WDW

chromeDriverPath='D:\chromeDriver\chromedriver.exe'#chromeDriver所在路径,务必保证chromedriver.exe的版本和浏览器版本一致
browser=webdriver.Chrome(executable_path = chromeDriverPath)#创建chrome浏览器控制器
browser.get('http://www.taobao.com/')#浏览器控制器访问网页
html=browser.page_source#直接获取网页源码
browser.close()#关闭浏览器

'''向搜索框输“台灯并搜索”'''
inputFirst=browser.find_element_by_id('q')#通过搜索标签id获取搜索框的网页源码
inputFirst.send_keys('台灯')#向输入框中输入’书包‘，搜索前务必登录淘宝
time.sleep(1)
inputFirst.click()

'''查找指定标签并获得相关内容'''
browser.find_elements_by_tag_name('div')#查找所有标签名为’div‘的标签
browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')#将页面拉到底部

print(inputFirst.get_attribute('class'))#获得标签inputFirst的'class'属性
print(inputFirst.text())#获得标签inputFirst的文本内容
inputFirst.location#返回标签位置
inputFirst.size#返回标签大小

'''网页前进和后退'''
browser.get('http://www.baidu.com/')
browser.get('http://www.taobao.com/')
browser.get('http://www.sina.com/')
browser.back()#后退一页
time.sleep(1)
browser.forward()#前进一页

'''切换选项卡'''
browser.get('http://www.baidu.com/')
browser.execute_script('window.open("http://www.sina.com/")')#再打开新浪网页
print(browser.window_handles)#打印所有网页窗口列表
browser.switch_to_window(browser.window_handles[1])#切换至第二个网页窗口
# =============================================================================
#爬取淘宝商品 
# =============================================================================
import bs4
import requests
import re

browser.get("http://www.7k7k.com/tag/62/new_1.htm#p-anchor")
html=browser.page_source
soup=BS(html,'html.parser')

#摘取一一页内容

contents=[]
for ul in soup.find_all('ul','ui-img-list cf lazyload-part')[:-1]:
    lis=ul('li')
    for li in lis:
        spans=li('span')
        tags=li('a')
        texts=''
        for tag in tags:
            text=tag.string
            texts=texts+str(text)
        name=spans[0].string
        date=spans[1].string                
        contents.append([name,date,texts[4:]])
len(contents)
# =============================================================================
#爬取7k7k小游戏(通过操控浏览器翻页，成功)
# =============================================================================
import requests
from bs4 import BeautifulSoup as BS
import time
from selenium import webdriver
import bs4
import requests
import re
import pandas as pd

chromeDriverPath='D:\chromeDriver\chromedriver.exe'#chromeDriver所在路径,务必保证chromedriver.exe的版本和浏览器版本一致
browser=webdriver.Chrome(executable_path = chromeDriverPath)#创建chrome浏览器控制器

#摘取一页内容
def getOnePage(html):
    soup=BS(html,'html.parser')
    for ul in soup.find_all('ul','ui-img-list cf lazyload-part')[:-1]:
        lis=ul('li')
        for li in lis:
            spans=li('span')
            tags=li('a')
            href=tags[0].get('href')
            texts=''
            for tag in tags:
                text=tag.string
                texts=texts+str(text)
            name=spans[0].string
            date=spans[1].string                
            contents.append([name,date,texts[4:],href])

#爬取多页内容
def getLotsPage(pageNumber):
    for i in range(pageNumber):
        browser.get("http://www.7k7k.com/tag/62/new_1.htm#p-anchor")
        html=browser.page_source            
        nextPage=browser.find_element_by_id('waterfall_next')
        nextPage.click()  
        time.sleep(1)
        getOnePage(html)
        print("已经爬取第"+str(i)+'页')
            

if __name__=='__main__':
    contents=[]
    getLotsPage(50)
    DATA=pd.DataFrame(contents,columns=['游戏名','发布日期','类型','网址'])
    DATA.to_excel('D:/python/代码运行文件夹/学习笔记/网络爬虫/爬取文件2/小游戏/7k7k小游戏.xlsx')

len(contents)
# =============================================================================
# 
# =============================================================================
"/yearbook/1999/p10c.htm"
data=pd.read_html('http://www.moe.gov.cn/jyb_xxgk/moe_1777/moe_1778/201906/t20190619_386539.html')












browser.find_element_by_name('p')








html=browser.page_source
soup=BS(html,'html.parser')
print(soup.prettify())





<img src="http://i2.7k7kimg.cn/cms/cms10/20191030/123111_6192.jpg" alt="机器人兄弟冒险" width="76" height="77">





from selenium import webdriver
browser = webdriver.Firefox()










soup=BS(html,'html.parser')
print(soup.prettify())
    