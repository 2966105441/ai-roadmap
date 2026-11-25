"""03.py —— 装上温度旋钮的对话程序"""
import argparse

from chat import ChatSession

parser = argparse.ArgumentParser()
parser.add_argument("--session", default="temp")
parser.add_argument("--plain", action="store_true")
parser.add_argument("--temp", type=float, default=0.7)
args = parser.parse_args()

s = ChatSession(args.session + ".json", args.temp)
print(f"（会话 {args.session}｜温度 {args.temp}｜流式回复）\n")

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
