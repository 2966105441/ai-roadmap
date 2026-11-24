"""03.py —— 装上自动截断的对话程序"""
import argparse

from chat import ChatSession

parser = argparse.ArgumentParser()
parser.add_argument("--session", default="trim")
parser.add_argument("--plain", action="store_true")
args = parser.parse_args()

s = ChatSession(args.session + ".json")
print(f"（会话 {args.session}｜流式回复）\n")

while True:
    text = input("你：")

    if text == "/quit":
        break
    elif text == "/clear":
        s.reset()
        print("  已清空\n")
    elif text == "/len":
        print(f"  本地 {len(s.history)} 条\n")
    elif text.strip():
        if args.plain:
            print("它：", s.send(text))
        else:
            print("它：", end="", flush=True)
            s.send_stream(text)
            print()
