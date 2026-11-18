import os
os.environ["NO_PROXY"] = "127.0.0.1,localhost"

import requests

payload = {"prompt": "小米 MiMo 是什么"}
r = requests.post("http://127.0.0.1:8000/chat", json=payload, timeout=5)

print(r.status_code)

data = r.json()
print(data["choices"][0]["message"]["content"])
print(data["usage"]["total_tokens"], "token")