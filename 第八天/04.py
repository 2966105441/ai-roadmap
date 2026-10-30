class Message:
    def __init__(self,role,content):
        self.role = role
        self.content = content

    def __str__(self):                    # 给人看：简洁、好看
        return f"[{self.role}]{self.content}"

    def __repr__(self):                  # 给程序员看：无歧义、能照着重建
        return f"Message(role={self.role!r},content={self.content!r})"


m = Message("user","你好")
print(str(m))             # 用 __str__
print(repr(m))            # 用 __repr__
print(m)                  # print 默认用 __str__
print([m])                # 放进列表，用的是 __repr__！