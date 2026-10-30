scores = [78,92,65,88]

total = 0
for s in scores:
    total += s

print("总分：",total)
print("平均：",total/len(scores))




scores = [78,92,65,88]
count = 0
for s in scores:
    if s >= 80:
        count += 1
print("80分以上的有",count,"个")



scores = [78,92,65,88]
best = scores[0]
for s in scores:
    if s > best:
        best = s
print("最高分：",best)

scores = [78, 92, 65, 88]
print(sum(scores), max(scores), min(scores))