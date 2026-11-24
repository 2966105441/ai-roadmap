"""01.py —— 不联网，先用一个列表把截断逻辑走一遍"""
MAX = 7
history = ["system", "u1", "a1", "u2", "a2", "u3", "a3"]
print("开始：", len(history), "条")

for text in ["u4", "a4", "u5", "a5"]:
    history.append(text)
    while len(history) > MAX:
        del history[1:3]
    print(f"加 {text} → {len(history)} 条  {history}")
