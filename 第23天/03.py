"""03.py —— 用一个列表攒历史，每轮都全发过去"""
import os

import requests

os.environ["NO_PROXY"] = "127.0.0.1,localhost"
URL = "http://127.0.0.1:8000/chat"
history = []


def chat(text: str) -> str:
    history.append({"role": "user", "content": text})
    resp = requests.post(URL, json={"messages": history}, timeout=10)
    reply = resp.json()["choices"][0]["message"]["content"]
    history.append({"role": "assistant", "content": reply})
    return reply


for q in ["什么是检索增强", "它有什么好处", "我一共问了几个问题"]:
    print("我：", q)
    print("它：", chat(q))
    print("   （现在历史里有", len(history), "条）")
    print()
