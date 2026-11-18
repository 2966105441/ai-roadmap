import os
os.environ["NO_PROXY"] = "127.0.0.1,localhost"

import requests

for p in ["你好", "小米 MiMo 是什么", "请用三句话解释什么是检索增强生成"]:
    r = requests.post("http://127.0.0.1:8000/chat", json={"prompt": p}, timeout=5)
    print(f"prompt 长度 {len(p):>2} -> total_tokens {r.json()['usage']['total_tokens']}")