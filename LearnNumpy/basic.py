#coding=utf-8
import numpy as np
'''
    Numpy学习 2017-3-11
    https://docs.scipy.org/doc/numpy-dev/user/quickstart.html
    分清哪个方法是深拷贝，哪个是返回视图，很重要！
'''

print('''-----Chapter One:The Basics-Array基本属性-----''')
print('''-----1.1 基本概念-----''')
'''
1.线性代数中都是二维矩阵和向量，矩阵维度指矩阵列数量，向量指列向量/行向量的列/行数量。
2.Numpy中是'超级矩阵'array，其不一定是2维矩阵，可以是n维的，为了区分将array维度称作axis。
3.一个维度是一个axis，维度的数量叫rank；例如下面a有三个axes，rank=3。
4.线性代数矩阵的rank=2，(行,列)数==a.shape，先行后列。
5.一个array中所有元素都是相同类型。a = np.array([[6,7],[9.0,1.0]])将会自动类型转换为float。
'''
a = np.arange(60).reshape(3,5,4)
#print(a)
print('number of axes',a.ndim)
print(a.shape)#array的每个axis的大小
print(a.size,3*5*4)
print(a.itemsize,type(a))
#print(a.data)#什么鬼？

print('''-----1.2 Array Creation-----''')
'''
1.从python:list,tuple创建
'''
a = np.array([[6,7,8],[9,10,11]])
print(a)
print(a.dtype)
#创建时指定类型
c = np.array( [ [1,2], [3,4] ], dtype=complex )
#创建指定大小的array
a = np.zeros((3,4))#用0占位
print(a)
a = np.ones((3,4),dtype=np.int16)#用1占位，并指定类型，默认是float64
print(a)
a = np.empty((3,4))#内存值是什么就是什么
print(a)
#arrange函数，类似Python的range函数，但是返回arrays。
a = np.arange(10,30,5)#from 10 to 小于30 gap 5
print(a)
a = np.linspace(0,2*np.pi,12)#9 numbers from 0 to 2
print(np.sin(a))

print('''-----1.3 Printing Arrays-----''')
'''
显示方式：
1.最后一个维度数据从左向右显示
2.倒数第二个维度数据从上向下显示(倒数两行构成了AXB的矩阵样子)
3.其余维度从上向下，由空行分隔(倒数第三行是矩阵的集合，由上到下，空行分隔相邻元素；倒数第四行是倒数第三行的集合，由上到下，空行分隔相邻元素；以此类推)
4.二维三维比较常用
the last axis is printed from left to right,
the second-to-last is printed from top to bottom,
the rest are also printed from top to bottom, with each slice separated from the next by an empty line.
'''
a = np.arange(12).reshape(2,2,3)
print(a)
#np.set_printoptions(threshold='nan')#设置完全显示array，否则太大了就不现实了

print('''-----1.4 Basic Operations ！！数学计算！！-----''')
'''
1.算数计算都是对每个元素操作；
2.矩阵运算要用dot函数
3.array运算结果都会存入新array，用+=可以就地保存
4.类型不同会向下类型转换
5.一元运算函数，指定运算作用的axis
'''
a = np.array([[20,30],[40,50]])
b = np.arange(4).reshape(2,2)
print(a+b)
print(a*b)
print(b**2)
print(b>0)
print(np.sin(b))
print(np.dot(a,b))
#一元运算，通过指定axis，使得运算只在指定axis上进行
a.sum()
a.min()
a.max()
a.sum(axis=0)

print('''-----1.5 Universal Functions-----''')
'''
See also:
all, any, apply_along_axis, argmax, argmin, argsort, average, bincount, ceil, clip, conj, corrcoef, cov, cross, cumprod, cumsum, diff, dot, floor, inner, inv, lexsort, max, maximum, mean, median, min, minimum, nonzero, outer, prod, re, round, sort, std, sum, trace, transpose, var, vdot, vectorize, where
'''
a = np.arange(3)
np.exp(a)
np.sqrt(a)
b = np.arange(-1,-4,-1)
print(a+b)
print(np.add(a,b))

print('''-----1.6 Indexing, Slicing and Iterating-----''')
'''
1.一维array的index和list差不多:
a[0],a[2:5],a[::-1]
for i in a:
    print(i)
2.多维array，每个元素的index是一个tuple，tuple第一个元素对应第一个axis坐标，以此类推。
因此，对于二维矩阵，a[2,3]表示的是第3行第四列。
3.迭代都是从第一个维度开始的，如下i是a[0,...]->a[-1,...]
for i in a:
    print(i)
4.for e in a.flat:#可以迭代每一个元素
    print(e)
5.假设a是3维的，枚举第二维的每个矩阵：#包含了枚举，切片，index
for i in range(a.shape[1]):
    print(a[:,i,:])
6.一般顶多2，3维，枚举也都是从第一个开始，后两维表示的是矩阵。
'''
a = np.arange(12).reshape(3,4)
print(a)
print(a[:,1])
print(a[2,3])
print(a[-1,...])
a = np.arange(24).reshape(2,3,4)
print(a)
for i in range(a.shape[1]):
    print(a[:,i,:])

print('''-----Chapter 2:Shape Manipulation-----''')
print('''-----2.1 Changing the shape of an array-----''')
'''
修改shape的过程可以看作是，先把新形状准备好，然后按照维度从左到右扫描原本的array，用元素填表
a.T是转置，和上面不一样。
'''
#下面的方法返回修改后的副本
a = np.arange(12).reshape(3,4)
print(a.ravel())#一维返回，flattened
print(a.reshape(12))#常用
print(a.T)#转置
#下面的方法直接就地修改array
a.resize(4,3)
print(a)
a.shape=3,4
print(a)

print('''-----2.2 Stacking together different arrays-----''')
'''
把array按照行/列拼接起来。好强！
'''
a = np.array([[1,1],[2,2]])
b = np.array([[3,3],[4,4]])
print(np.vstack((a,b)))#vertical垂直，注意输入是tuple
print(np.hstack((a,b)))#horizontal水平，注意输入是tuple
print(np.column_stack((a,b[:,1])))#和np.hstack()差不多啊

'''-----2.3 Splitting one array into several smaller ones-----'''
'''
完全不懂！
https://docs.scipy.org/doc/numpy-dev/user/quickstart.html#splitting-one-array-into-several-smaller-ones
'''

print('''-----Chapter3:Copies and Views-----''')
'''
1.像是index，slice这些返回的都是视图，即之前所有方法，没有说是返回一个新的array的，其实都是返回视图。
2.视图就是看起来是什么的意思呗，操作视图会修改原始数据的。
3.返回新array就是深拷贝。b = a.copy()
4.检查是相同对象不同引用，还是相同对象的视图，还是没指向相同对象，可以使用
    d is a#True则同对象不同引用，False则可能是不同对象也可能相同对象的不同视图
    d.base is a#True相同对象不同视图，False不同对象
5.方法总结：
Array Creation
    arange, array, copy, empty, empty_like, eye, fromfile, fromfunction, identity, linspace, logspace, mgrid, ogrid, ones, ones_like, r, zeros, zeros_like
Conversions
    ndarray.astype, atleast_1d, atleast_2d, atleast_3d, mat
Manipulations
    array_split, column_stack, concatenate, diagonal, dsplit, dstack, hsplit, hstack, ndarray.item, newaxis, ravel, repeat, reshape, resize, squeeze, swapaxes, take, transpose, vsplit, vstack
Questions
    all, any, nonzero, where
Ordering
    argmax, argmin, argsort, max, min, ptp, searchsorted, sort
Operations
    choose, compress, cumprod, cumsum, inner, ndarray.fill, imag, prod, put, putmask, real, sum
Basic Statistics
    cov, mean, std, var
Basic Linear Algebra
    cross, dot, outer, linalg.svd, vdot
6.本小节：
https://docs.scipy.org/doc/numpy-dev/user/quickstart.html#copies-and-views
'''

print('''-----Chapter4:进阶操作-----''')
'''
见这里吧，先不看了，看了也记不住
https://docs.scipy.org/doc/numpy-dev/user/quickstart.html#less-basic
'''