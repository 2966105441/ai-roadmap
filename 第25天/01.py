"""01.py —— 痛点：一份全局 history，两个会话没法同时用"""
import os

import requests

os.environ["NO_PROXY"] = "127.0.0.1,localhost"
URL = "http://127.0.0.1:8000/chat"
history = []


def chat(who: str, text: str) -> str:
    history.append({"role": "user", "content": f"{who}：{text}"})
    resp = requests.post(URL, json={"messages": history}, timeout=10)
    reply = resp.json()["choices"][0]["message"]["content"]
    history.append({"role": "assistant", "content": reply})
    return reply


print("A：", chat("A", "你好"))
print("B：", chat("B", "你好"))
print("A：", chat("A", "我刚才说了什么"))
print()
print("history 一共", len(history), "条，A 和 B 的话混在一起")
