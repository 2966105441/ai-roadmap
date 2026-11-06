import jieba
jieba.add_word("向量数据库")
s = "我在向量数据库做检索"
print(jieba.lcut(s))