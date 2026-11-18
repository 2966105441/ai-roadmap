import os
os.environ["NO_PROXY"] = "127.0.0.1,localhost"

import functools
import time
from dataclasses import dataclass
from typing import Any

import requests

BASE = "http://127.0.0.1:8000"


class ApiError(Exception):
    """接口出错时统一抛这个，外面只认它"""


@dataclass
class Reply:
    url: str
    status: int
    seconds: float
    data: Any


def retry(times: int = 3, wait: float = 1.0):
    """带参数的装饰器：写 @retry(times=3) 就重试 3 次"""
    def deco(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(1, times + 1):
                try:
                    return func(*args, **kwargs)
                except ApiError as e:
                    print(f"  第 {i} 次失败：{e}")
                    if i == times:
                        raise
                    time.sleep(wait)
        return wrapper
    return deco


@retry(times=3, wait=1.0)
def fetch_json(url: str, timeout: float = 5.0) -> Reply:
    t0 = time.time()
    try:
        r = requests.get(url, timeout=timeout)
    except requests.exceptions.Timeout:
        raise ApiError(f"{timeout} 秒内没有响应")
    except requests.exceptions.ConnectionError:
        raise ApiError("连不上服务")
    if r.status_code >= 400:
        raise ApiError(f"HTTP {r.status_code}")
    return Reply(url=url, status=r.status_code,
                 seconds=round(time.time() - t0, 3), data=r.json())


def main():
    rep = fetch_json(BASE + "/flaky")
    print(f"成功　状态 {rep.status}　耗时 {rep.seconds}s")
    print("内容：", rep.data)

    rep = fetch_json(BASE + "/stats.json")
    d = rep.data
    print(f"\n{d['source']}：{d['total']} 词 / {d['distinct']} 个不同词")
    for i, item in enumerate(d["top"], 1):
        print(f"  {i}. {item['word']:<4}{item['count']}")


if __name__ == "__main__":
    main()