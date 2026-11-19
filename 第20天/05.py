"""05.py —— 把第 15 天的词频统计，包成一个能收参数的命令行工具"""
import argparse
import jieba

parser = argparse.ArgumentParser(description="中文词频统计")
parser.add_argument("input", help="文本文件路径")
parser.add_argument("-n", "--top", type=int, default=8, help="显示前几名，默认 8")
args = parser.parse_args()

PUNCT = "。，、！？；：“”‘’（）…—"
with open("../data/stop_words_zh.txt", encoding="utf-8") as f:
    STOP = {ln.strip() for ln in f if ln.strip() and not ln.startswith("#")}

with open(args.input, encoding="utf-8") as f:
    text = f.read()

counter = {}
for w in jieba.lcut(text):
    w = w.strip(PUNCT).strip()
    if w and w not in STOP:
        counter[w] = counter.get(w, 0) + 1

print(f"来源：{args.input}    不同词数：{len(counter)}")
for w, c in sorted(counter.items(), key=lambda kv: -kv[1])[:args.top]:
    print(f"{w:<6}{c:3}")
