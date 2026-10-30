def add_item(item,box=[]):
    box.append(item)
    return box


print(add_item("a"))
print(add_item("b"))
print(add_item("c"))

#正确写法：默认写 None，进函数再建
def add_item(item,box=None):    # 默认值是 None（不可变）
    if box is None:               # 没传 → 每次新建一个
        box = []
    box.append(item)
    return box
print(add_item("a"))
print(add_item("b"))

# 记住这个固定套路：默认值写 None，函数第一行判断 if xxx is None: xxx = []。以后所有"默认给个空容器"的场景都这么写。
# 注意是 is None 不是 == None。is 判断"是不是同一个东西"，None 全宇宙只有一个，所以用 is。