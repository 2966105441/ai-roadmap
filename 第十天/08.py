import jieba

t1 = "大语言模型可以写代码"
t2 = "检索增强生成可以解决这个问题。"

print("--- 默认词典 ---")
print(jieba.lcut(t1))
print(jieba.lcut(t2))

#把你行业的词告诉jieba
jieba.add_word("大语言模型")
jieba.add_word("检索增强生成")

print("--- 加词之后 ---")
print(jieba.lcut(t1))
print(jieba.lcut(t2))