#numpy库
import numpy as np
#利用array创建数组
# a=np.array([2,4,8,20,16,30])
# b=np.array(((1,2,3,4,5),(6,7,8,9,10)))
# print("一维数组：",a)
# print("二维数组:\n",b)
#一维数组： [ 2  4  8 20 16 30]
#二维数组:
 #[[ 1  2  3  4  5]
 #[ 6  7  8  9 10]]
#利用arrange,empty,linspace等函数生成数组
# a=np.linspace(0,2,5)
# b=np.mgrid[0:2:5j]
# x,y=np.mgrid[0:2:4j,10:20:5j]
# print("x={}\ny={}".format(x,y))
# a=np.random.randint(1,11,(3,5))#生成[1,10]区间上3行5列的随机整数数组
# print(a)
# print("维数：",a.ndim)
# print("维度：",a.shape)
# print("元素总数:",a.size)
# print("类型:",a.dtype)
# print("每个元素字节数：",a.itemsize)
# a=np.arange(0,3,0.5).reshape(2,3)#生成2x3的数组
# np.savetxt('Pdata2_18_1.txt',a)#按照'%.18e'的格式保存数值，以空格分隔
# b=np.loadtxt("Pdata2_18_1.txt")
# print("b=",b)
# np.savetxt("Pdata2_18_2.txt",a,fmt="%d",delimiter=",")
# c=np.loadtxt("Pdata2_18_2.txt",delimiter=",")
# print("c=",c)




