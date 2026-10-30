# 方法：挂在对象身上的函数
# 方法就是写在类里面的函数，唯一的区别是第一个参数固定是 self，所以它能直接摸到对象身上的数据。
class Message:
    def __init__(self,role,content):
        self.role = role
        self.content = content

    def to_dict(self):                           # 方法：不用传 role/content，它身上就有
        return {"role":self.role,"content":self.content}

    def length(self):
        return len(self.content)

    def __str__(self):
        return f"[{self.role}]{self.content}"


m = Message("user","你好呀")
print(m.to_dict())
print(m.length())
print(str(m))

msgs = [Message("user","你好"),Message("assistant","在")]
for x in msgs:
    print(str(x))




