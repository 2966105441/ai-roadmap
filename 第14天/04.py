import csv

rows = [{"姓名": "张三", "电话": "13800001111"},
        {"姓名": "李四", "电话": "13900002222"}]

# A：不加 newline=""
with open("a.csv", "w", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=["姓名", "电话"])
    w.writeheader()
    w.writerows(rows)

# B：加了 newline=""
with open("b.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["姓名", "电话"])
    w.writeheader()
    w.writerows(rows)

print("A 的字节：", repr(open("a.csv", "rb").read()[:30]))
print("B 的字节：", repr(open("b.csv", "rb").read()[:30]))