import pandas as pd
import numpy as np
import os
import tushare as ts
pro=ts.pro_api('7fac027f24db4e9bddd02e3f998cd48f9f28551050860e2c402d87fc')
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['simhei']#用于正常显示中文标签
plt.rcParams['axes.unicode_minus']=False#用于正常显示负号
data=pro.daily(ts_code='600036.SH',start_date='20190607',end_date='20191011')#获取股票日收盘价数据
data=pd.DataFrame(data)#只有将数据转化为DataFrame格式，在操作数据时才可以出现pandas函数的自动提示

#基本操作
if 'basic'=='basic':
       data.columns#Index(['ts_code', 'trade_date', 'open', 'high', 'low', 'close', 'pre_close','change', 'pct_chg', 'vol', 'amount']
       data.index
       data.shape#数据框的行列数
       data.info()#统计数据的信息
       data[['open', 'high', 'low', 'close']].apply(lambda x: x * 2)  # 对所有数据进行乘2运算
       data.dtypes#统计数据框中的数据类型
       pd.set_option('display.max_columns', None)# 显示所有列
       pd.set_option('display.max_rows', None)# 显示所有行
       np.set_printoptions(suppress=True)#若想不以科学计数显示:

       pd.cut(np.random.randint(1, 90, 200), 4)
       pd.Categorical([1, 2, 3, 1, 2, 3])
       pd.CategoricalIndex(np.random.choice(['a', 'b', 'c', 'd', 'e'], 100))
       int = pd.Interval(2, 6)

#修改行列标题
if 'index_columns'=='index_columns':
       data.index=pd.date_range('20120201',periods=len(data['vol']),freq='D')#修改数据框的行标题
       data.columns=['股票代码', '交易日期', '开盘价', '最高价', '最低价', '收盘价', '前日收盘价','收盘价变动', 'pct_chg', '交易量', '交易额']#
       data.rename(columns={'open':'开盘价'},inplace=True)

#添加行列数据
if 3==3:
       data['kk']=0#添加数值为0的'kk'列
       data.ix['另一行',:]=0#添加数值为0的'另一行'行

#选取数据
if 'select'=='select':
       data['high']
       data[4:9]
       data[['open', 'high', 'low', 'close']]
       data['ts_code'].str[:4]#选取股票代码前四个字符，只有字符串类型的数据才可以作此操作
       data.head(8)  # 选取数据前8行
       data.tail(8)  # 选取数据后8行

#利用ix()函数选取数据
if 'ix'=='ix':
       data.ix[3:5]#选取第4到5行数据
       data.ix[3:8,4:6]#选取第4到8行数据，第3到6列数据
       data.ix[5]#选取第6行数据
       data.ix[:,5]#选取所有行，第6列
       data.ix[:,'ts_code']#选取所有行，标题为'ts_code'的数据
       data.ix[:,'ts_code':'high']#选取所有行，列标题从'ts_code'到'high'的数据
       data.ix[[3,4]]#选取第4,5行的数据
       data.ix[[2,6],[5,7]]#选取第3,7行，第6,8列的标题
       data.ix[[2,5],'ts_code']#选取第3,6行，列标题为'ts_code'的数据
       data.ix[[4,6],['trade_date', 'open', 'high']]#选取第5,7行的，列标题为'trade_date', 'open', 'high'的数据
       data.ix[1]#选取第二行

#选取指定条件的数据
if '>'=='>':
       data.ix[data['open']>=35]#选取'open'中所有大于35的数据
       data.ix[data['open']>=35,[2,3]]#选取'open'中所有大于35的数据中的第3,4列
       data[(data['open']>=35)&(data['open']<=35.7)]#选取‘open’中大于35且小于35.7的数据
       data[(data['open']<=35)|(data['open']>=35.7)]#选取‘open’中小于35或大于35.7的数据
       data[(data['open']<=35)]

#drop函数删除
if 'drop'=='drop':
       data.drop('open',axis=1)#删除指定列标题
       data.drop('open',axis=1,inplace=True)#永久删除列标题
       data.drop(['change', 'pct_chg', 'vol'],axis=1)
       data.drop(data.columns[1:6],axis=1)
       data.drop(4,axis=0)#按照行标题删除数据

#作图
if 'plt'=='plt':
       plt.scatter(data.index,data['close'])
       plt.pie(data['open'],shadow=True,colors='g')
       plt.scatter(data.index,data['high'],edgecolors='r',linewidths=0.5,alpha=0.5,color='p')
       plt.title('HIGH_PRICE')

       if 'plot'=='plot':#同时绘制多条序列折线图
              plt.figure(num=2, figsize=(20, 10), facecolor='y', edgecolor='r')
              plt.plot(data['交易日期'], data[['open', 'high', 'close', 'low']])
              plt.xticks(rotation=270)
              plt.show()

       if 'box'=='box':#绘制箱线图
              data_box = data[['open', 'high', 'close', 'low']]
              plt.figure(figsize=(20, 10))
              plt.boxplot(data_box, meanline=True)

#数学统计
if 'math'=='math':
       data.describe()#按照列数据进行统计描述
       data.cov()#构建各列之间的协方差矩阵
       data.corr()#构建各列之间的相关系数矩阵
       data.corrwith(data['high'])#构建“最高价”列数据与所有列数据的相关系数
       data.min()#产生各列的最小值
       data.max()#最大值
       data.mean()#均值
       data.median()#中位数
       data.std()
       data.round(3)#保留三位小数
       data.skew()#计算偏度
       data.kurt()#计算峰度

#对无效值的处理
if 'null'=='null':
       '''删除法'''
       sum(pd.isnull(data))  # 统计数据表各列无效数值个数
       data.dropna()  # 将直接删除所有包含无效数据的行
       data.dropna(how='all')  # 只删除全行皆为无效数据的行

       '''填补法'''
       data.fillna(7)  # 使用7来替换所有无效数据
       data.fillna(method='ffill')  # 使用上面的数据进行填充
       data.fillna(method='bfill')  # 使用后面的数据进行填充
       data.fillna({'三': 3, '四': 2, '五': 1, })  # 不同的列用不同的数值填充
       data = data.fillna({'三': data_2['八'].mean, '四': data_2['四'].median, '五': 1, })  # 通过中位数和平均值进行填充

#数据拼接组合
if 'combine'=='combine':
       data_1=pro.daily(ts_code='600036.SH',start_date='20190607',end_date='20191011')#获取股票日收盘价数据
       data_2 = pro.daily(ts_code='600136.SH', start_date='20190607', end_date='20191011')  # 获取股票日收盘价数据
       data_columns=pd.concat([data_1,data_2],axis=0)#按照行的方向进行拼接
       data_row=pd.concat([data_1,data_2],axis=1)#按照列的方向进行拼接

       #可以将列标题不同的数据框进行拼接
       if 'lost'=='lost':
              data_1.drop('ts_code',axis=1,inplace=True)
              data_lost=pd.concat([data_2,data_1],axis=0)
              data_lost['close']

              data_1=pd.DataFrame(np.random.rand(3,4),index=[1,2,3],columns=['A','B','C','E'])
              data_2=pd.DataFrame(np.random.rand(4,5),index=[1,2,4,5],columns=['A','D','C','E','F'])
              data_lost_1=pd.concat([data_1,data_2],axis=0)
              data_lost_2 = pd.concat([data_1, data_2], axis=1)

#数据透视表和多层索引
if 'many'=='many':
       #构造多层索引数据框
       if 1==1:
              #将A对应'一','二','三'，将B对应'四','五'
              data=pd.DataFrame(np.random.rand(6,5),index=[['A','A','A','B','B','C'],['一','二','三','四','五','六']],columns=[['甲','甲','乙','乙','乙'],['one','two','one','two','three']])
              data.ix['A','甲']
              data['甲']
              data.ix['A',:]

       #为普通数据框添加外部索引
       if 2==2:
              data=pd.DataFrame({'loc':np.random.choice(['a','b','c','d','e'],80),
                                   'age':np.random.randint(34,45,80),
                                 'six':np.random.choice(['男','女'],80),
                                 'high':np.random.randint(150,187,80),
                                 'money':np.random.normal(3000,40,80)})


              data_=pd.pivot_table(data,index=['six','loc','age'])#按照'six','loc','age'的顺序
              data_=pd.pivot_table(data,index=['six','loc','age'],values=['money'])
              data_ = pd.pivot_table(data, index=['loc'], values=['money'],aggfunc=[np.sum,np.min])




#对时间的处理
if "datetime"=="datetime":
       import datetime,time
       if "常用格式"=="常用格式":
             """
             % a 星期几的简写
              % A 星期几的全称
              % b 月分的简写
              % B 月份的全称
              % c 标准的日期的时间串
              % C 年份的后两位数字
              % d 十进制表示的每月的第几天
              % D 月 / 天 / 年
              % e 在两字符域中，十进制表示的每月的第几天
              % F 年 - 月 - 日
              % g 年份的后两位数字，使用基于周的年
              % G 年分，使用基于周的年
              % h 简写的月份名
              % H 24小时制的小时
              % I 12小时制的小时
              % j 十进制表示的每年的第几天
              % m 十进制表示的月份
              % M 十时制表示的分钟数
              % n 新行符
              % p 本地的AM或PM的等价显示
              % r 12小时的时间
              % R 显示小时和分钟：hh: mm
              % S 十进制的秒数
              % t 水平制表符
              % T 显示时分秒：hh: mm:ss
              % u 每周的第几天，星期一为第一天 （值从0到6，星期一为0）
              % U 第年的第几周，把星期日做为第一天（值从0到53）
              % V 每年的第几周，使用基于周的年
              % w 十进制表示的星期几（值从0到6，星期天为0）
              % W 每年的第几周，把星期一做为第一天（值从0到53）
              % x 标准的日期串
              % X 标准的时间串
              % y 不带世纪的十进制年份（值从0到99）
              % Y 带世纪部分的十制年份
              % z， % Z 时区名称，如果不能得到时区名称则返回空字符。
              % % 百分号
             """


       today=datetime.date.today().strftime('%Y%m%d')#获取今天日期
       yesterday = (datetime.date.today() + datetime.timedelta(days=-1)).strftime('%Y%m%d')#获取昨天日期
       this_month=datetime.date.today().strftime('%Y%m')#获取这个月的日期
       now_time = datetime.datetime.now()#获取现在时间
       hour=now_time.strftime('%H')#显示当前几点

#类的测试
if 'class'=='class':
       class Test():
              def __init__(self):
                     self.h=5

              def print_A(self):
                     print('A')
                     print(self.h)

              def print_B(self):
                     self.print_A()
                     print('B')

       test=Test()
       test.print_A()
       test.print_B()





