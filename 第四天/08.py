line = "自然语言处理 是 人工智能 的 一个 重要 分支"
words = line.split()  # 不带参数：按空白切
print(words)
print(len(words))

#带参数的split：按指定的符号切
print("a,b,c".split(","))
print("2026-10-26".split("-"))
#注意切出来的全是字符串——'2026' 是文字不是数字


#join:把列表拼回一串
words = ["自然语言处理","是","AI","的","重要","分支"]
print("-".join(words))
print(" ".join(words))
print("".join(words))
