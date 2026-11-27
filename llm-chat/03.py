"""03.py —— 一句话变一条数据，攒成一个真文件"""
import json

from client import extract        # client.py 里新加的，一次抽一条

TEXTS = ["明天交周报", "下周准备组会", "把这个脚本跑一遍"]

items = []
for t in TEXTS:
    item = extract(t)             # 已经是字典了，不是字符串
    print(f"{item['title']}｜截止 {item['due']}")
    items.append(item)

with open("notes.json", "w", encoding="utf-8") as f:
    json.dump(items, f, ensure_ascii=False, indent=2)

print(f"\n存了 {len(items)} 条到 notes.json")
