import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
plt.rcParams['font.sans-serif']=['simhei']#用于正常显示中文标签
plt.rcParams['axes.unicode_minus']=False#用于正常显示负号

'''各种图形'''
if __name__=='__main__':
    plt.plot()#折线图
    plt.bar()#条形图
    plt.scatter()#散点图
    plt.hist()#直方图
    plt.pie()#绘制饼状图
    plt.boxplot()#箱型图

'''单图单线'''
if 'one(one)'=='one(one)':
    data_1=-90*np.random.beta(23,41,400)#生成服从贝塔分布的随机数据
    plt.figure(figsize=(8,6),dpi=80)#设置画板大小
    plt.grid(True)#设置网格线
    plt.title('贝塔分布',fontsize=33,color='r',alpha=0.5)#设置标题
    plt.plot(np.arange(len(data_1)),data_1,linewidth=2,color='g',label='贝塔数值')#绘制折线图，线粗度为2，颜色为绿色
    plt.axis([3,300,np.min(data_1),np.max(data_1)])#设置两个坐标轴的长度范围
    plt.xticks([3,73,143,213,283],rotation=270,color='y')#使得横轴显示指定刻度，旋转270度，颜色为黄色
    plt.yticks([-40,-30,-20,-10],color='y')#使得纵轴显示指定刻度，颜色为黄色
    plt.xlabel('范围',color='y',fontsize=25)#设置x轴标签
    plt.ylabel('贝塔分布数值',color='y',fontsize=25)#设置y轴标签
    plt.text(74,data_1[73],'amazing',size=18,rotation=-40,ha='left',va='bottom')#在横轴为74的地方添加文字备注
    plt.fill_between(np.arange(len(data_1))[73:143],data_1[73:143],data_1[73:143]-20,facecolor='y',alpha=0.3)#填充73:143之间的区域
    plt.legend(loc='upper right',fontsize='small')#在右上方的位置生成图例，字体较小，需要通过plt.plot()中的label函数输入图例文字
    plt.show()
    plt.savefig('贝塔分布.pdf',transparent=True)#将背景设置为透明

'''单图作多线'''
if 'one(two)'=='one(two)':
    sin_random=3*np.sin(np.arange(-10,10,0.1))+np.random.normal(0,2,200)
    cos_random=3*np.cos(np.arange(-10,10,0.1))+np.random.normal(0,2,200)+3
    plt.figure(num=2,figsize=(16,8),facecolor='y')
    plt.plot(np.arange(-10,10,0.1),sin_random,label='sin随机数')#只需要在一个框架下作两次plot()即可
    plt.plot(np.arange(-10,10,0.1),cos_random,label='cos随机数')
    plt.legend(loc='upper right')
    plt.title('sin函数和cos函数随机分布',fontsize=30,color='r',alpha=0.6)
    plt.grid(True,color='g',alpha=0.2)
    plt.xlabel('序数',fontsize=30)
    plt.ylabel('随机数值',fontsize=30)
    plt.fill_between(np.arange(-10,10,0.1)[30:150],sin_random[30:150],cos_random[30:150],alpha=0.4)
    plt.show()



"""多图"""
if __name__=='__main__':
    data=pd.DataFrame(np.arange(1,101),columns=['序号'])
    data['贝塔分布']=np.random.beta(3,6,100)
    data['鳄鱼分布']=np.random.exponential(3,100)
    data['卡方分布']=np.random.chisquare(5,100)
    data['伽马分布']=np.random.gamma(1,6,100)

    plt.figure(num=3,figsize=(12,8))
    plt.suptitle=('随机数图')
    plt.subplot(2,2,1)
    plt.title('贝塔分布散点图')
    plt.scatter(data['序号'],data['贝塔分布'],alpha=0.5,edgecolors='y')
    plt.subplot(2,2,2)
    plt.title('贝塔分布散点图',color='y')
    plt.scatter(data['序号'],data['贝塔分布'],alpha=0.5,edgecolors='y')
    plt.subplot(2,2,3)
    plt.title('贝塔分布散点图',color='g')
    plt.scatter(data['序号'],data['贝塔分布'],alpha=0.5,edgecolors='y')
    plt.subplot(2,2,4)
    plt.title('贝塔分布散点图',color='b')
    plt.scatter(data['序号'],data['贝塔分布'],alpha=0.5,edgecolors='y')

"""概率分布图"""
if 'scipy'=='scipy':
    data = np.random.chisquare(14, 8000)#构造服从卡方分布的随机数据
    ax=sns.distplot(data, bins=100, kde=True, color='b', hist_kws={"linewidth": 15, 'alpha': 0.4})#将数据分为100组，绘制概率分布图，kde=True可以绘制出概率密度曲线
    ax.set(xlabel='Normal Distribution', ylabel='Frequency')








