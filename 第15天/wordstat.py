"""把词频统计的结果用 dataclass 表达"""
import json
from dataclasses import dataclass, field


@dataclass
class WordStat:
    """一个词 + 它出现的次数"""
    word: str
    count: int

    @property
    def pct(self) -> float:
        return self.count / self.total * 100 if self.total else 0.0

    total: int = field(default=0, repr=False, compare=False)


@dataclass
class Report:
    """一份完整的词频报告"""
    source: str
    total: int
    stats: list[WordStat] = field(default_factory=list)

    def top(self, n: int = 5) -> list[WordStat]:
        return sorted(self.stats, key=lambda s: -s.count)[:n]

    def to_json(self) -> str:
        return json.dumps(
            {"source": self.source,
             "total": self.total,
             "top": [{"word": s.word, "count": s.count} for s in self.top(3)]},
            ensure_ascii=False, indent=2)