citys = ["北京","上海","武汉","郑州"]
print(citys[0])
print(citys[-1])

citys.append("杭州")
citys.insert(1,"西安")
print(citys)

for i,f in enumerate(citys,start=1):
    print(f"第{i}个城市：{f}")



sums = [78,92,65,88,95]
print(f"总分：{sum(sums)}")
print(f"平均分：{sum(sums)/len(sums):.2f}")


max_1 = sums[0]
for i in sums:
    if i > max_1:
        max_1 = i
print(f"最大值为{max_1}")

count = 0
for i in sums:
    if i>60:
        count+=1
print(f"及格人数：{count}")


