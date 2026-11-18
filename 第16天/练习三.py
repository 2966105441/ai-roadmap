import os
os.environ["NO_PROXY"] = "127.0.0.1,localhost"

import requests


def safe_get(url, timeout=5):
    try:
        r = requests.get(url, timeout=timeout)
        r.raise_for_status()
        return r.json()
    except requests.exceptions.RequestException as e:
        print(f"  放弃：{type(e).__name__}")
        return None


print("正常：", safe_get("http://127.0.0.1:8000/hello"))
print("404 ：", safe_get("http://127.0.0.1:8000/nope"))
print("超时：", safe_get("http://127.0.0.1:8000/slow", timeout=1))