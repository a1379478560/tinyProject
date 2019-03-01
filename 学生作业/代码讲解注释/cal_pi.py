
#第一题

from random import random   #random是产生随机数的函数
from math import  sqrt  #sqrt是开方函数
from time import clock  #程序里似乎没有用到
'''
这个程序要搞懂用随机数计算Pi的得原理
就是画一个正方形，然后在正方形内画一个最大的内切圆，然后随机的往里面扔点（x，y坐标由random函数产生，并且一定在正方形内）
这个点落在圆里面的话hits就增加一，
最后计算落在圆里的概率是多大，根据这个计算   落在圆里的点/总点数=圆的面积/正方形面积，圆的面积是2*Pi*r~2  其他值都已知，由此就可以计算pi值
这里的正方形边长是1，然后将圆简化成了四分之一圆（这样就不用考虑x，y为负的情况），
也就是这里其实是一个边长为1的正方形里面有一个最大的四分之一圆，原理是与整圆一样的，所以后面有乘四
'''

darts=20000.0   #设定循环次数，也就是实验次数 ，次数是随意的但是越多越准确，精度越高，耗时也越长
hits=0.0  #初始化在圆内的点的个数
for i in range(1, int(darts)):   #循环darts次
    x,y = random(), random()     #随机产生一个点，random（）产生（0,1）内的小数
    dist = sqrt(x**2+y**2)     #计算距离圆心的距离，为下面判断是否在圆内做准备
    if dist <=1.0:              #如果在圆内就让hits加一
        hits = hits + 1
        pi = 4 * (hits/darts)   #这里是他把我上面写的公式简化得来的，因为正方形边长跟圆的半径都是1，所以式子看着很简洁，实际上他不用每部都计算一个pi值，最后计算一次即可，也就是把这句前边的两个缩进都删了也可以。效率更高
print(pi)  #输出结果


#第二题
'''
这个题是把华氏温度跟摄氏温度互转，根据输入的温度最后一个字符是c还是f来判断原本的温度是什么类型的，然后
根据转换公式来计算
'''
val = input('please enter a temprature number（such as 32c）：')   #输入要转换的值
if val[-1] in ['c','C']:    #判断如果最后一个字符是或者C，那就是 摄氏度转华氏度
    f = 1.8 * float(val[0:-1]) + 32  #摄氏度转华氏度公式         这个val[0:-1]跟上面的val[-1]都是python里面的叫切片的特性，不知道的话看这里 https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431756919644a792ee4ead724ef7afab3f7f771b04f5000
    print('transformed temperature is %.2f F' %f)   #输出结果    %.2f是控制输出的精度为两位，舍去两位后面的
elif val[-1] in ['f','F']:         #最后一位是f或者F的情况，跟上面类似
    c = (float(val[0:-1]) - 32)/1.8   #上面公式的逆运算
    print('transformed temperature %.2f C' %c)
else:
    print('what you enter is not a temperature number')



#第三题
import requests   #这是一个请求网页的库，用来拿到网页的源代码
import re    #正则库，用来搜索有效信息
goods = 'bag'  #定义搜索关键词
page = 0   #爬取第几页
start_url = 'https://s.taobao.com/search?q=' + goods    #这是淘宝的搜索地址，你可以去搜索一个商品看看上方网址，就是这个格式的
url = start_url + '&s=' + str(44*page)   #这也是淘宝的商品显示公式，一页显示44个商品，加上前面的start_url就是完整的某一页商品的url
r = requests.get(url, timeout=30)#用requests库获取网页对象
html=r.text  #r.text是这个网页对象的源代码部分
plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"',html)  #用正则表达式在网页源代码里搜索页面内有用的信息，下面也是，至于搜索的关键词是要根据网页内容而定的
tlt = re.findall(r'\"raw_title\"\:\".*?\"',html)       #这块不知道为什么搜索这个的话打开淘宝搜索页面的源代码看看，找找规律
for i in range(len(plt)):    #循环输出搜索到的信息
    price = eval(plt[i].split(':')[1])  #eval是把括号里面的字符串当做公式或者程序源代码去执行。（这个函数很危险）
    title = eval(tlt[i].split(':')[1])
    print(price)   #输出结果
    print(title)



#第四题
import matplotlib.pyplot as plt   #matplotlib是一个类似MATLAB的python库，可以理解成python版的matlab   这个程序是画了一个简单的图，图的形状在程序里面有  x=***  y=***nali
import numpy as np   #numpy是一个处理数据数组矩阵的库，常用在科学计算
import matplotlib
matplotlib.rcParams['font.family']='STSong'   #设置字体 xxSong应该是什么宋体
matplotlib.rcParams['font.size']='16'  #设置字号
x=np.arange(0,5,0.02)  #这个是numpy里面的函数，返回0到5，步长0.02的一个数组，也就是横坐标是0-5，最小精度0.02
y=np.exp(-x)*np.cos(2*np.pi*x)  #计算某一横坐标的纵坐标值， exp（-x）是e的-x次幂  cos你懂的
plt.plot(x,y)   #根据上面给的公式计算，绘制出图
plt.xlabel('time') #x轴标签
plt.ylabel('amplitude') #y轴标签
plt.show()  #显示图
