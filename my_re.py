# -*- coding: utf-8 -*-
"""一、正则表达式简介
　　正则表达式是一个特殊的字符序列，它能帮助你方便的检查一个字符串是否与某种模式匹配。 Python 自1.5版本起增加了re 模块，它提供 Perl 风格的正则表达式模式。
　　就其本质而言，正则表达式（或 RE）是一种小型的、高度专业化的编程语言， （在Python中）它内嵌在Python中，并通过 re 模块实现。正则表达式模式被 编译成一系列的字节码，然后由用 C 编写的匹配引擎执行。
　　re 模块使 Python 语言拥有全部的正则表达式功能。 compile 函数根据一个模式字符串和可选的标志参数生成一个正则表达式对象。该对象拥有一系列方法用于正则表达式匹配和替换。 re 模块也提供了与这些方法功能完全一致的函数，这些函数使用一个模式字符串做为它们的第一个参数。"""


import re
# =============================================================================
# 二，字符匹配
# =============================================================================
"""普通字符"""#大多数字符和字母都和自身相匹配
re.findall('ks','dfkjaslfjaskdjksjfisjfks')
#Out[292]: ['ks', 'ks']  
#寻找出所有查找的字符

"""元字符"""# .   ^   $   *   +   ?   { }   [ ]   |   ( )  \

#. 匹配除了换行符以外的任意一个字符
re.findall('.','dkfjl')
#Out[293]: ['d', 'k', 'f', 'j', 'l']

#^ 只有后面跟的字符在开头，才能匹配上
re.findall('^hk','fkdhkjdjf')
#Out[294]: []
re.findall('^ji','jianlddjfn')
#Out[295]: ['ji']

#$ 只有前面的字符在结尾才能匹配上
re.findall('hf$','kojhf')
#Out[297]: ['hf']

#* 它前面那个字符出现0——n次都可以匹配上
re.findall('hl*','dfhijfdfhllksfdjksfhl')
#Out[298]: ['h', 'hll', 'hl']

#+ 它前面那个字符出现1——n次都可以匹配上
re.findall('dfh+','dfhhhsjflsjfdfhfh')
#Out[300]: ['dfhhh', 'dfh']

#? 匹配前面那个字符出现0或1次
re.findall("alexsel?","aaaalexse")
#Out[301]: ['alexse']

#{} 将它前面的字符匹配出现指定次数
re.findall('gh{2}','ghhhkdhfghkdjfg')
#Out[302]: ['ghh']
re.findall('dhf{2,5}','dhfffsdfhdhfffff')
#Out[303]: ['dhfff', 'dhfffff']  将f匹配2——5次

#\ 后面跟元字符去除元字符特殊功能，跟普通字符产生特殊功能
re.search('\.','hfdkjf.')
re.findall('\^','fhdsk^^')#去除^的特殊功能，当成普通字符进行匹配
text='sfkh\\\\dfjd'
re.findall(r'\\',text)#r可以直接表示\\为字符\\，不需要间接转义
re.findall('\\\\',text)#\\通过\将\的特殊含义去除，单纯表示字符\


#\d 匹配十进制数字，相当于[0-9]
re.findall('\d4','hfd45fdsf34')
#Out[316]: ['34']

#\D 匹配任何非十进制数字，相当于[^0-9]
re.findall('[^3-5]','62743648323647')#匹配非3-5的数字
re.findall('\D','jdfldsjf8379dflkj3yk')
re.findall('(\D)*','dffkjdf76fds')

#\s 匹配任何空白字符，相当于[ \t\n\r\f\v]
re.findall('[2-5]\s','3 454 435325')
re.findall('\D\s','  dfs sf cv fg5 ')
#Out[336]: ['  ', 's ', 'f ', 'v ']

#\S 匹配任何非空白字符，相当于[^ \t\n\r\f\v]
re.findall('\S{3}','dfhskdjf jldkf')
#Out[337]: ['dfh', 'skd', 'jld']

#\w 匹配任何数字字母字符，相当于[0-9a-zA-Z]
re.findall('s\w*','dfjsfljdsfsdf')
#Out[339]: ['sfljdsfsdf']

#\W 匹配任何非数字字母字符，相当于[^0-9a-zA-Z]
re.findall('.\W','含fsjf djf村 jdkl')

#\b 表示匹配一个单词的边界，即单词和空格之间的位置
re.findall('\\bcost\\b','cost fjdk cost df')#需要再增添一个\将\b正常操作
re.findall(r'\bcost\b','cost fjdk cost df')#通过加r使\b可以独立发挥作用
re.findall(r'sin\b','sindsin dsfs')
re.findall(r'kit\b','kit*dfsf')#单词边界不一定是空格，可以是特殊字符

#() 将括号内的内容当作一个整体去处理
re.findall('(23)(45)','2323233223234523')#寻找23或45
re.findall('(\d+)','yhrf3yij54i5784thi48')

# 通过添加?实现非贪婪匹配,将+和*只能匹配一次
re.findall('\d+?','34325345')
re.findall('[0-9][a-z]+?','3h43kjh43u5h4j5h4u')
#Out[394]: ['3h', '3k', '3u', '5h', '4j', '5h', '4u']
re.findall('[0-9][a-z]+','3h43kjh43u5h4j5h4u')
#Out[394]: ['3h', '3kjh', '3u', '5h', '4j', '5h', '4u']

# =============================================================================
# 三，常用函数
# =============================================================================
#re.match函数只在字符串开头匹配一下，如果没有便失败
re.match('jw','isdfheiwuhewiru389rjw;e,r/43to oujfp3;,r 32ir239yr31hir 3rpi30tu p3tro40t').group()
re.match('is','isdfheiwuhewiru389rjw;e,r/43to oujfp3;,r 32ir239yr31hir 3rpi30tu p3tro40t').group()

#re.search函数可以在整个字符串上进行匹配
re.search('(\d)','isdfheiwuhewiru389rjw;e,r/43to kiiioujfp3;,r 32ir239yr31hir 3rpi30tu p3tro40t').group()
re.search(r'\d','isdfheiwuhewiru389rjw;e,r/43to kiiioujfp3;,r 32ir239yr31hir 3rpi30tu p3tro40t').groups()

#re.compile() 将匹配这个过程定义下来
recs=re.compile('c\d')#具有匹配字符‘c数字’的功能

text1='c43ksjdcsjfsljc45sjflsjfsc2sfdd'
text2='dfjsldfjudsic833fy8c832'
recs.findall(text1)
recs.findall(text2)


















re.findall('\\\\','\\\\')
re.findall(r'\','')
re.match('a\\\j','a\\\jdkk').group



mm = "c:\\a\\b\\c"                                                      
re.match(r"c:\\",mm).group()





re.findall('.3','742394734k32h')
re.findall('f.d{1}','dlfsjflsdhfksjkfsdjfkjs')
re.findall('')

text='''2) marxist dialectics
Marxist dialectics
1.
Deng Xiaoping going Stage of Marxist Dialectics: A Philosophical Consideration of the 30 th Anniversary of China s Reform and Opening - up;
The stage of deng xiaoping theory of marxist dialectics -- philosophical reflection on the 30th anniversary of reform and opening up
2.
Going with practice and analysis with short and the consistency of logic and history of Marxist dialectics to explain the basic going and on the characteristics and reasonable of the existing Thinking modes to carry out the review and on this basis to establish the location and dialectical thinking of the an innovate thinking modes.
In this paper, the basic theory of marxist dialectics is discussed by combining theory with practice, analysis with synthesis, logic with history'''
re.findall('\d[a-z]',text)







#() 将()内的字符当成一个整体进行匹配
re.findall('(kc)(h)','kchkchjd')
#Out[305]: [('kc', 'h'), ('kc', 'h')]
re.findall('t(ca)+','tcacacacat')

# =============================================================================
# 通过正则表达式匹配信息
# =============================================================================
import re
import requests
import bs4
from bs4 import BeautifulSoup as BS
import pandas as pd

#下载源码
r=requests.get('https://beijing.baixing.com/gongzuo/?src=topbar')
r.status_code
r.encoding=r.apparent_encoding
html=r.text
soup=BS(html,'html.parser')
soup.prettify()

#匹配需要信息
regrex="<li><p class='title'><a href='https://beijing.baixing.com/[a-z]*/a\d*\.html\?src=[a-zA-Z]*' target='_blank'>(.{5,35})</a><span class='salary'>(\d*-\d*元)</span></p><p class='detail-info'><span class='job-name'>([^a-zA-Z0-9]*)</span><span class='address'>([^a-zA-Z0-9]*)</span><span class='compnay-name'>([^a-zA-Z0-9]*)</span></p><p class='welfare'><span class='tags'>([^a-zA-Z0-9]*)</span><span class='tags'>([^a-zA-Z0-9]*)</span><span class='tags'>([^a-zA-Z0-9]*)</span></p></li>"
data0=re.findall(regrex,html)
data0=list(data0)
DATA=pd.DataFrame(data0)


# =============================================================================
# 
# =============================================================================

url='https://beijing.baixing.com/gongzuo/'
r=requests.get(url)
r.status_code
r.encoding=r.apparent_encoding
html=r.text
soup=BS(html,'html.parser')
soup.prettify()


re.search('scr[a-z]pt',html)#返回第一个匹配结果
re.split('c',html[:1000])#讲字符串按照c进行分割
re.match('.',html[:100])
# =============================================================================
# 
# =============================================================================




import re
import inspect
import os
print(os.path.abspath(inspect.getfile(re.match)))

help(sub())
help(int)

import os
dir(os)











