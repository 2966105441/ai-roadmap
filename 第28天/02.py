"""02.py —— 把字从流里抠出来，一个字一个字打"""
import json

import requests
import time
URL = "http://127.0.0.1:8000/chat_stream"

resp = requests.post(URL, json={"prompt": "你好"}, stream=True, timeout=10)

t0 = time.time()
first = True

for line in resp.iter_lines(decode_unicode=True):
    if not line or not line.startswith("data: "):
        continue
    data = line[6:]
    if data == "[DONE]":
        break
    piece = json.loads(data)["choices"][0]["delta"]["content"]
    if first:
        print(f"[首字 {time.time() - t0:.2f} 秒]", flush=True)
        first = False
    print(piece, end="", flush=True)
print()
