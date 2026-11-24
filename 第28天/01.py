"""01.py —— 先看清「流」长什么样"""
import requests

URL = "http://127.0.0.1:8000/chat_stream"

resp = requests.post(URL, json={"prompt": "你好"}, stream=True, timeout=10)

for i, line in enumerate(resp.iter_lines(decode_unicode=True)):
    if i < 10:                      # 只打前 10 行，后面长得一模一样
        print(repr(line))
