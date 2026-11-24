"""02.py —— 换成类：每个会话带着自己的 history"""
import os

import requests

os.environ["NO_PROXY"] = "127.0.0.1,localhost"
URL = "http://127.0.0.1:8000/chat"

class ChatSession:
    def __init__(self):
        self.history = []

    def send(self, text: str) -> str:
        self.history.append({"role": "user", "content": text})
        resp = requests.post(URL, json={"messages": self.history}, timeout=10)
        reply = resp.json()["choices"][0]["message"]["content"]
        self.history.append({"role": "assistant", "content": reply})
        return reply


a = ChatSession()
b = ChatSession()
print("A：", a.send("你好"))
print("B：", b.send("你好"))
print("A：", a.send("我刚才说了什么"))
