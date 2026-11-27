score = [78,92,55,88,61,95,43,70,84,59]
print(f"平均分 {sum(score)/len(score):.1f}")
print(f"最高:{max(score)}  最低:{min(score)}")
Number = 0
fail = []
for i in score:
    if i >= 60:
        Number += 1
    else:
        fail.append(i)
print(f"及格 {Number}/{len(score)}")
print(f"前三{sorted(score,reverse=True)[:3]}")
print(f"不及格{fail}")
