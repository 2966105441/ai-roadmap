"""02.py —— 一边聊一边存，关掉再打开还接得上"""
from chat import ChatSession

s = ChatSession("work.json")
print("（输入「再见」结束）\n")

while True:
    text = input("你：")

    if text == "再见":
        break

    print("它：", s.send(text))
    print()
