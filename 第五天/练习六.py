shuju = {"张三":92,"李四":78,"王五":88}
f_1 = shuju["李四"]
for k,v in shuju.items():
    if v > f_1:
        k_1 = k
        f_1 = v
print(f"最高分为：{k_1}({f_1})")
