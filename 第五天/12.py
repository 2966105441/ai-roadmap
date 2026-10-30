#元组
point = (3,5)       #圆括号
print(point)
print(point[0],point[-1])
print(len(point))


#point[0] = 99   #这行会报错：元组改不了

#最有用的功能：一次拆成多个变量
x,y = point
print("x =",x,"y =",y)
#用一句话记：元组就是把列表冻结起来。取值、切片、len、in 全都一样，唯一区别是不能改——没有 append，不能赋值。