#集合：自动去重，但不保顺序
s = {1,2,2,3,3,3}
print(s)
print(len(s))

#实用场景：一个列表里有多少个不同的词
words = ["AI","是","AI","的","AI"]
print(set(words))
print("不同词数：",len(set(words)))

# 还有一个陷阱：empty = {} 建出来的是空字典，不是空集合。空集合要写 set()。这个错很多人犯。


