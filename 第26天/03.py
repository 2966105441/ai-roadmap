"""03.py —— 换个名字，就是另一段对话"""
import argparse

from chat import ChatSession

parser = argparse.ArgumentParser(description="跟模型聊天")
parser.add_argument("--session", default="default", help="会话名字，换名字就是另一段对话")
args = parser.parse_args()

s = ChatSession(args.session + ".json")
print(f"（当前会话：{args.session}，输入「再见」结束）\n")

while True:
    text = input("你：")

    if text == "再见":
        break

    if not text.strip():
        continue

    print("它：", s.send(text))
    print()
