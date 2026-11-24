"""01.py —— 给聊天程序加两个命令"""
import argparse

from chat import ChatSession

parser = argparse.ArgumentParser()
parser.add_argument("--session", default="default")
args = parser.parse_args()

s = ChatSession(args.session + ".json")
print(f"（会话 {args.session}｜输入 /help 看命令）\n")

while True:
    text = input("你：")

    if text == "/quit":
        break
    elif text == "/help":
        print("  /help  看这个   /quit  退出\n")
    elif text.strip():
        print("它：", s.send(text))
        print()
