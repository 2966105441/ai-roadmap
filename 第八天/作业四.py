class Message:
    def __init__(self,role,content):
        self.role = role
        self.content = content

    def to_dict(self):
        return {"role": self.role,"content":self.content}

    def __str__(self):
        return f"[{self.role}]{self.content}"

class Chat:
    def __init__(self):
        self.messages = []

    def add(self,role,content):
        self.messages.append(Message(role,content))

    def show(self):
        for m in self.messages:
            print(m)

    def to_list(self):
        return [m.to_dict() for m in self.messages]

c = Chat()
c.add("system","你是一个助手")
c.add("user","你好")
c.add("assistant","你好，有什么可以帮您")
c.show()
print(c.to_list())  