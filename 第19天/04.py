"""04.py —— 列表里套字典，自动变成对象（第 17 天练习三那个 AttributeError）"""
from pydantic import BaseModel


class WordStat(BaseModel):
    word: str
    count: int


class Report(BaseModel):
    source: str
    total: int
    stats: list[WordStat]


rep = Report(source="sample_zh.txt", total=82,
             stats=[{"word": "检索", "count": "6"}])
print("stats[0] 的类型 =", type(rep.stats[0]).__name__)
print(rep.stats[0].word, rep.stats[0].count, "| count 也自动转成了", type(rep.stats[0].count).__name__)
