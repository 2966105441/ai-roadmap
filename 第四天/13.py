fruits = ["苹果","香蕉","橙子"]
for i in range(len(fruits)):
    print(i,fruits[i])


fruits = ["苹果","香蕉","橙子"]

for i,f in enumerate(fruits):
    print(i,f)

print("--- 编号从1开始 ---")
for i,f in enumerate(fruits,start=1):
    print(f"第{i}个：{f}")