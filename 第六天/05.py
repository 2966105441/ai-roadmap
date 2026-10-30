# return：今天真正的重点
# 这是新手最容易混的一对：print 和 return。很多人写了三个月代码，以为函数的结尾就该是 print。看这个实验：

def add_print(a,b):
    print(a+b)                 # 打印出来，但没有交出去

def add_return(a,b):
    return a+b                 # 计算完，把结果交出去

x = add_print(3,5)        # 屏幕上会打印 8
print(f"print版拿到的值是：{x}")

y = add_return(3,5)         # 屏幕上什么都不打印
print(f"return版拿到的值是：{y}")
print(f"还能继续算：{y * 2}")


# 看出差别了吗？用一张表说清楚：
#                     print	                                    return
# 结果去哪	          屏幕（给人看）	                            调用它的地方（给程序用）
# 能被                 x = ... 接到吗	不能，接到的是 None	    能，接到真实结果
# 能继续参与运算吗	  不能	                                    能，y * 2 就是 16
# 什么时候用	          最后给人看结果	                            中间过程一律用这个


# 函数内部处理数据用 return，只在最外层用 print 给用户看。
# 如果你写的函数一半 print 一半 return，它就是个"半成品"——既不能当工具复用，又污染屏幕。你昨天通讯录里所有函数都直接 print，所以那些代码没法被别的程序调用。
