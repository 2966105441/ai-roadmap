"""main.py —— 命令行聊天入口

先另开一个终端跑 fake_server.py，再跑这个。
"""
import argparse

from client import ChatSession

parser = argparse.ArgumentParser()
parser.add_argument("--session", default="chat")
parser.add_argument("--plain", action="store_true")
parser.add_argument("--temp", type=float, default=0.7)
args = parser.parse_args()

s = ChatSession(args.session + ".json", args.temp)
mode = "非流式" if args.plain else "流式"
print(f"（会话 {args.session}｜温度 {args.temp}｜{mode}）\n")

while True:
    text = input("你：")

    if text == "/quit":
        break
    elif text == "/clear":
        s.reset()
        print("  已清空\n")
    elif text == "/len":
        print(f"  本地 {len(s.history)} 条\n")
    elif text.startswith("/temp "):
        s.temperature = float(text.split()[1])
        print(f"  温度改成 {s.temperature}\n")
    elif text.strip():
        if args.plain:
            print("它：", s.send(text))
        else:
            print("它：", end="", flush=True)
            s.send_stream(text)
            print()
