class Message:
    def __init__(self,role,content):
        self.role = role
        self.content = content

m = Message("user","你好")
print(m.role,"|",m.content)
print(type(m))
print(m)


m2 = Message("assistant","你好呀")
print(m2.role,m2.content)
print("m和m2是两个不同对象：",m is m2)

#坑一
class Msg:
    def __init__(self,text):
        self.text = text    #忘了self
m = Msg("你好")
print(m.text)

#坑二
class A:
    def hi(self):
        return "hi"
print(A().hi())