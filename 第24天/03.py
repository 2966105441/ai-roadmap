"""03.py —— 每聊一轮就写一次文件"""
import json
import os

import requests

os.environ["NO_PROXY"] = "127.0.0.1,localhost"
URL = "http://127.0.0.1:8000/chat"
FILE = "chat.json"

with open(FILE, encoding="utf-8") as f:
    history = json.load(f)

for q in ["它有什么好处", "那它有什么缺点"]:
    history.append({"role": "user", "content": q})
    resp = requests.post(URL, json={"messages": history}, timeout=10)
    reply = resp.json()["choices"][0]["message"]["content"]
    history.append({"role": "assistant", "content": reply})
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(history, f, ensure_ascii=False, indent=2)
    print(f"（存完，文件里 {len(history)} 条）它：", reply)
