import requests
import re
from bs4 import BeautifulSoup as BS
import bs4


kv={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362'}#Mozilla/5.0是一个标准的浏览器
url='http://lishi.zhuixue.net/#'    
r=requests.get(url,headers=kv)
r.status_code
r.encoding=r.apparent_encoding
html=r.text
soup=BS(html,'html.parser')
print(soup.prettify)

print(soup.title)#打印题目
print(soup.title.name)#打印标题标签名字
print(soup.title.string)#打印标题尖括号之间的内容
print(soup.title.parent.name)#打印title标签父标签的名字
print(soup.p)#打印第一个p标签（含内容）
print(soup.p['class'])#打印第一个p标签及class属性
print(soup.a['href'])#打印第一个a标签的href属性值
print(soup.p.contents)#输出第一个p标签的所有子节点
print(soup.find_all('a'))#获得所有标签名为a的标签
print(soup.find_all('ul',"xiaobiaoti"))#输出所有名为ul，属性值为"xiaobiaoti"的标签
print(soup.find_all(target="_blank"))#输出所有target="_blank"的标签
print(soup.get_text())#输出所有文本内容（尖括号之间的文字）
print(soup.a.attrs)#输出第一个标签的所有属性信息（字典）

for link in soup.find_all('a'):#获得所有标签a的href属性
    print(link.get('href'))

for child in soup.p.children:#对标签p的子节点进行循环输出
    print(child)

# 修改第一个 a 标签的href属性为 http://www.baidu.com/
# soup.a['href'] = 'http://www.baidu.com/'

# 给第一个 a 标签添加 name 属性
# soup.a['name'] = u'百度'

# 删除第一个 a 标签的 class 属性为
# del soup.a['class']

##输出第一个 p 标签的所有子节点
print(soup.p.contents)
















