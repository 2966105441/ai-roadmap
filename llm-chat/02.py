"""02.py —— 模型说它输出的是 JSON，但直接 load 就炸"""
import json
import os

import requests

os.environ["NO_PROXY"] = "127.0.0.1,localhost"
URL = "http://127.0.0.1:8000/extract"

for i in range(3):
    resp = requests.post(URL, json={"text": "明天交周报"}, timeout=10)
    raw = resp.json()["choices"][0]["message"]["content"]
    print(f"--- 第 {i + 1} 次，开头 12 个字：{raw[:12]!r}")
    try:
        print(f"    直接 loads：成功，due = {json.loads(raw)['due']}")
    except json.JSONDecodeError as e:
        print(f"    直接 loads：炸了 → {e}")
    start, end = raw.find("{"), raw.rfind("}")
    print(f"    洗过之后：成功，due = {json.loads(raw[start:end + 1])['due']}\n")
