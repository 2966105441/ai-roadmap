"""02.py —— 回来的是一坨 JSON，得一层层剥"""
import os

import requests

os.environ["NO_PROXY"] = "127.0.0.1,localhost"

url = "http://127.0.0.1:8000/chat"
resp = requests.post(url, json={"prompt": "什么是 RAG"}, timeout=5)
data = resp.json()

print("所有键：", list(data.keys()))
print("模型：", data["model"])
print("回复：", data["choices"][0]["message"]["content"])
print("花了多少 token：", data["usage"]["total_tokens"])
