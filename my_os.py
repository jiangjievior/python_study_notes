# =============================================================================
# 获取当前工作文件夹地址
# =============================================================================
import os
"""获取路径"""
os.getcwd()# 获取当前工作文件夹路径
os.path.abspath('.') #获取当前工作目录路径
os.path.abspath('test.txt') #获取当前目录文件下的工作目录路径
os.path.abspath('..') #获取当前工作的父目录 ！注意是父目录路径
os.path.abspath(os.curdir) #获取当前工作目录路径

"""改变当前工作路径"""
import os
os.chdir('图形开发界面')#修改当前文件夹路径为'图形开发界面'（修改的文件夹必须在当前目录中）
os.chdir('..')#返回上一层文件夹路径
os.makedirs('zh/ddf/kf')#创建文件夹，多层文件夹
os.removedirs('ddf/kf')#删除指定文件夹
os.rmdir('kf')#只能删除一个单级空文件夹
os.listdir('D:\python\代码运行文件夹\学习笔记')#列出指定文件夹中所有的文件和文件夹以及隐藏文件
os.remove('新建位图图像.bmp')#删除指定文件
os.rename('类','类简介')#修改文件名或文件夹名
os.stat('类简介')#查看一个文件的详细信息
os.listdir()#获得指定文件夹下所有文件名

os.path.isfile(path)#判断是否文件
os.path.isdir(path)#判断是否目录
os.path.exists(path)#判断路径是否存在


os.sep#输出当前路径分隔符
os.linesep#输出当前操作系统的行终止符
os.pathsep#输出当前操作系统的路径分隔符

os.path.getmtime('D:\python\代码运行文件夹\学习笔记')#返回最后修改时间

os.path.dirname('ddf')
os.path.basename('D:\python')#返回最后一级目录
os.path.abspath('矩阵运算.py')
os.chdir('sklearn机器学习')

#遍历指定目录下的所有文件夹和文件(务必将目录切换至目标文件夹所在目录)
item=os.walk('与excel交互')
type(item)#是一个迭代器
for i in item:
    print(i)
#返回一个元组，分别包含 文件路径 其中的文件夹 其中的文件

#文件路径和文件名的折分与合并
#拆分：
dirname, filename = os.path.split('D:\\python_code\\split_functon.py')
print(dirname,filename)
#结果输出为：dirname= D:\python_code ; filename= split_functon.py
#合并：
filepath = os.path.join('D:\\python_code', 'split_functon.py')
a=print(filepath)
#结果输出为：D:\python_code\split_functon.py


os.makedirs('D:\python\代码运行文件夹\学习笔记\os模块\joi')
path=os.getcwd()
path=os.path.join(path,'test')
os.makedirs(path)
os.chdir(path)

if __name__=='__main__':
    os.getcwd()
    os.makedirs('.\shiyan')
    os.path.abspath('my_os.py')





































