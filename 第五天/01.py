names = ["张三","李四","王五"]
scores = [92,78,88]

idx = names.index("李四")
print(scores[idx])

for n,s in zip(names,scores):
    if n == "李四":
        print(s)

