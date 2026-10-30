#刚才说"函数里改不了外面的变量"，但列表和字典能改：
def add_one(items):
    items.append(1)

nums = []
add_one(nums)
print(f"函数外：{nums}")

def rebind(items):
    items = items + [1]

nums2 = []
rebind(nums2)
print(f"重新赋值后：{nums2}")

# 一句话记住
# = 在函数里创建新变量（不影响外面）；.append() / .pop() / d[k]=v 修改原对象（影响外面）。
# 这跟你 Day 004 学的 "b = a 不是复制，是多配了一把钥匙" 是同一件事：传参传的是钥匙，不是保险箱。改箱子里的东西大家都看得见，换箱子只有你自己知道。