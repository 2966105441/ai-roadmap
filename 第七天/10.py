count = {"the":11,"retrieval":5,"and":4}

#把（词，次数）反过来,变成（次数,词）
pairs = []
for w,c in count.items():
    pairs.append((c,w))
print(pairs)


#元组排序是"先比第一个，相同再比第二个"
pairs.sort(reverse=True)
print(pairs)