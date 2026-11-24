"""01.py —— 连问两次，看看它记不记得上一句"""
import os

import requests

os.environ["NO_PROXY"] = "127.0.0.1,localhost"
URL = "http://127.0.0.1:8000/chat"


def ask(prompt: str) -> str:
    resp = requests.post(URL, json={"prompt": prompt}, timeout=10)
    return resp.json()["choices"][0]["message"]["content"]


print("我：什么是检索增强")
print("它：", ask("什么是检索增强"))
print()
print("我：我刚才问了你什么？")
print("它：", ask("我刚才问了你什么？"))
