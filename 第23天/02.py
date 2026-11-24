"""02.py —— 手动把三条消息塞过去，看看它认不认"""
import os

import requests

os.environ["NO_PROXY"] = "127.0.0.1,localhost"
URL = "http://127.0.0.1:8000/chat"

messages = [
    {"role": "user", "content": "什么是检索增强"},
    {"role": "assistant", "content": "就是先查资料，再回答"},
    {"role": "user", "content": "我刚才问了你什么？"},
]

resp = requests.post(URL, json={"messages": messages}, timeout=10)
print("它：", resp.json()["choices"][0]["message"]["content"])
