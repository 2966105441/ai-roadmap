class Msg:
    tags = []

    def __init__(self,text):
        self.text = text
    def __str__(self):
        return f"{self.text!r}"
a = Msg("第一条")
b = Msg("第二条")
print(a)
a.tags.append("重要")
print("a.tags =",a.tags)
print("b.tags =",b.tags)
print("是同一个列表吗：",a.tags is b.tags)


class Msg:
    def __init__(self,text):
        self.text = text
        self.tags = []       #每造一个对象，都新建一个空列表

a = Msg("第一条")
b = Msg("第二条")
a.tags.append("重要")
print("a.tags =",a.tags)
print("b.tags =",b.tags)
print("是同一个列表吗：",a.tags is b.tags)
# 类属性适合放所有对象共享、而且不会改的常量，比如 MAX_TOKENS = 4096。只要是可变对象（列表、字典、集合），一律放 __init__ 里。