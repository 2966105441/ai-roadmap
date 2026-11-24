"""03.py —— 两个会话、两份文件，各聊各的"""
from chat import ChatSession

a = ChatSession("chat_a.json")
b = ChatSession("chat_b.json")

print("A：", a.send("你好"))
print("B：", b.send("你好"))
print("A：", a.send("我刚才说了什么"))
print("B：", b.send("我刚才说了什么"))
print()
print("A 的文件里", len(a.history), "条 | B 的文件里", len(b.history), "条")
