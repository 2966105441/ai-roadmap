text = "自然语言处理 是 人工智能 的 一个 重要 分支 它 研究 如何 让 计算机 理解 人类 语言"
words = text.split()
print(f"总词数：{len(words)}")
print()

# 第 2 步：挑出长度 ≥3 的词（短词多是虚词，没啥信息量）
long_words = []
for w in words:
    if len(w) >= 3:
        long_words.append(w)
print(f"长度≥3的词：{long_words}")
print(f"共{len(long_words)}个，占{len(long_words)/len(words):.0%}")
print()

#第三步：算平均步长
total_len = 0
for w in words:
    total_len += len(w)
print(f"总字数：{total_len}")
print(f"平均词长：{total_len/len(words):.2f}")
print()

#第四步：按词长从长到短排，看前5名
words.sort(key=len,reverse=True)

print("按词长排序：")
for i,w in enumerate(words[:5],start=1):
    print(f"{i}.{w}({len(w)}字)")