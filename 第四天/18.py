names = ["张三","李四","王五","赵六"]
scores = [92,78,58,88]
print(zip(names,scores))
for name,score in zip(names,scores):
    if score >= 90:
        level = "优秀"
    elif score >= 80:
        level = "良好"
    elif score >= 60:
        level = "及格"
    else:
        level = "不及格"
    print(f"{name}:{score}分->{level}")
