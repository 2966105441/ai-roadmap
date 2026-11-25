"""01.py —— 不联网，看「温度」到底在干什么"""
import math
import random

PHRASES = ["好的。", "嗯，接着说。", "行，聊聊。", "我听着呢。", "这有意思，然后呢？"]
LOGITS = [3.0, 2.2, 1.6, 1.0, 0.4]       # 模型给这五个候选打的分


def pick(t):
    """按温度从五个候选里抽一个"""
    exps = [math.exp(x / t) for x in LOGITS]   # 温度越小，分差被放大得越狠
    return random.choices(PHRASES, weights=exps)[0]


for t in [0.1, 0.7, 2.0]:
    picks = [pick(t) for _ in range(20)]
    print(f"\n温度 {t}")
    for p in PHRASES:
        print(f"  {p}  {picks.count(p)} 次")
