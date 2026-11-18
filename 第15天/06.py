import jieba
from wordstat import WordStat, Report

jieba.add_word("检索增强生成")
jieba.add_word("大语言模型")
jieba.add_word("提示词")

PUNCT = ".,!?;:'\"()。，、！？；：“”‘’（）…—"

STOP = set()
with open("../data/stop_words_zh.txt", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if line and not line.startswith("#"):
            STOP.add(line)

text = open("../data/sample_zh.txt", encoding="utf-8").read()
counter = {}
for w in jieba.lcut(text):
    w = w.strip(PUNCT)
    if not w.strip() or w in STOP:
        continue
    counter[w] = counter.get(w, 0) + 1

total = sum(counter.values())
stats = [WordStat(word=w, count=c, total=total) for w, c in counter.items()]
rep = Report(source="sample_zh.txt", total=total, stats=stats)

print(f"来源：{rep.source}")
print(f"总词数：{rep.total}    不同词数：{len(rep.stats)}")
print("-" * 40)
for i, s in enumerate(rep.top(8), 1):
    print(f"{i:2}. {s.word:<6} {s.count:3}  {s.pct:5.1f}%")
print("-" * 40)
print(rep.to_json())
