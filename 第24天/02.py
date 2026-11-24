"""02.py —— 启动时把历史读回来，接着上次聊"""
import json
import os

import requests

os.environ["NO_PROXY"] = "127.0.0.1,localhost"
URL = "http://127.0.0.1:8000/chat"

with open("chat.json", encoding="utf-8") as f:
    history = json.load(f)

print("从文件读回来", len(history), "条")

history.append({"role": "user", "content": "我刚才问了你什么？"})
resp = requests.post(URL, json={"messages": history}, timeout=10)
print("它：", resp.json()["choices"][0]["message"]["content"])
