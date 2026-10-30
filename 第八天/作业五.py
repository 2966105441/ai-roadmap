class ChatGood:
    def __init__(self):
        self.messages = []

class ChatBad:
    messages = []
    def __init__(self):
        pass

a,b = ChatGood(),ChatGood()
print("正确写法，同一个列表吗：",a.messages is b.messages)

x,y = ChatBad(),ChatBad()
print("错误写法，同一个列表吗：",x.messages is y.messages)
x.messages.append("张三说的话")
print("y的对话里也有：",y.messages)
