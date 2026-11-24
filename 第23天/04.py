"""04.py —— 加一条 system，给模型先定个规矩"""
import os

import requests

os.environ["NO_PROXY"] = "127.0.0.1,localhost"
URL = "http://127.0.0.1:8000/chat"
history = [{"role": "system", "content": "你是一个只回答一句话的助手。"}]


def chat(text: str) -> str:
    history.append({"role": "user", "content": text})
    if len(history) > 4:
        del history[1:3]  # 砍掉最早的一问一答，system 留着
    n = len(history)
    resp = requests.post(URL, json={"messages": history}, timeout=10)
    data = resp.json()
    reply = data["choices"][0]["message"]["content"]
    history.append({"role": "assistant", "content": reply})
    print(f"   （发了 {n} 条，花了 {data['usage']['total_tokens']} token）")
    return reply


print("它：", chat("什么是检索增强"))
print()
print("它：", chat("它有什么好处"))
