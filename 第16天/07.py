import os
os.environ["NO_PROXY"] = "127.0.0.1,localhost"

import time
import requests


def 重试(func):
    def wrapper(*args, **kwargs):
        for i in range(1, 4):
            try:
                r = func(*args, **kwargs)
                if r.status_code < 500:
                    return r
                print(f"  第 {i} 次失败：{r.status_code}，等 1 秒重试")
            except requests.exceptions.RequestException as e:
                print(f"  第 {i} 次出错：{type(e).__name__}，等 1 秒重试")
            time.sleep(1)
        raise RuntimeError("试了 3 次都不行")

    return wrapper


@重试
def get(url):
    return requests.get(url, timeout=5)


r = get("http://127.0.0.1:8000/flaky")
print("最终：", r.status_code, r.json())