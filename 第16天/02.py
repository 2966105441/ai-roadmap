import os
os.environ["NO_PROXY"] = "127.0.0.1,localhost"

import requests

r = requests.get("http://127.0.0.1:8000/stats.json",timeout=5)
data = r.json()

print(type(data))
print(data["source"],data["total"],data["distinct"])

for item in data["top"]:
    print(f'   {item["word"]:<4}{item["count"]}')


if "json" in r.headers.get("content-type",""):
    data = r.json()
else:
    print("对方给的不是JSON，是：",r.text[:100])
    