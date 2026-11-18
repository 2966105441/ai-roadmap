import os
os.environ["NO_PROXY"] = "127.0.0.1,localhost"

import requests

r = requests.get("http://127.0.0.1:8000/hello", timeout=5)

print("Content-Type:", r.headers["Content-Type"])
print("Server:", r.headers.get("Server"))
print("我发出去的 UA:", r.request.headers["User-Agent"])




try:
    requests.get("http://127.0.0.1:8000/slow", timeout=1)
except requests.exceptions.Timeout:
    print("1秒没等到，放弃了")
    