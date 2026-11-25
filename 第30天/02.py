"""02.py —— 同一个问题，三个温度，各问 5 次"""
import requests

URL = "http://127.0.0.1:8000/chat"

for t in [0.1, 0.7, 2.0]:
    print(f"\n== 温度 {t} ==")
    for _ in range(5):
        resp = requests.post(URL, json={"prompt": "你好", "temperature": t}, timeout=10)
        print("  ", resp.json()["choices"][0]["message"]["content"])
