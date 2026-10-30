#作用域：函数里的变量，外面看不见
count = 100           #全局变量（外面定义的）
def show():
    count = 5              #这叫”新建了一个局部变量“，不是”改外面的“
    print(f"函数内：{count}")

show()
print(f"函数外:{count}")

#重点：函数里的 count = 5 并没有改变外面的 count，而是在函数内部造了一个同名的新变量。函数结束时它就被销毁了，外面那个 100 从头到尾没被动过。

# total = 0
# def add_one():
#     total = total + 1
#
# add_one()
#「你在函数里给 total 赋值了，所以我把它当成局部变量。但你等号右边又用了 total 的值，而这时候它还没被赋值。」


#正确做法是把值传进去、把结果 return 出来，而不是偷偷改全局变量：
def add_one(n):
    return n + 1
total = 0
total = add_one(total)     #按住返回值，重新赋值
print(total)               #1

