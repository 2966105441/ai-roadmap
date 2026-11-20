"""05.py —— 用 pydantic 接住 /stats.json"""
import os

import requests
from pydantic import BaseModel

os.environ["NO_PROXY"] = "127.0.0.1,localhost"


class WordStat(BaseModel):
    word: str
    count: int


class Stats(BaseModel):
    source: str
    total: int
    distinct: int
    top: list[WordStat]


resp = requests.get("http://127.0.0.1:8000/stats.json", timeout=5)
s = Stats(**resp.json())

print(f"{s.source}：共 {s.total} 个词，不同 {s.distinct} 个")
for w in s.top:
    print(f"  {w.word:<6}{w.count:3}")