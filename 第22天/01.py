"""01.py —— 先把话发出去：POST 一个 JSON 给模型"""
import os

import requests

os.environ["NO_PROXY"] = "127.0.0.1,localhost"

url = "http://127.0.0.1:8000/chat"
resp = requests.post(url, json={"prompt": "你好，介绍一下自己"}, timeout=5)

print("状态码：", resp.status_code)
print("回来的原文：")
print(resp.text)
