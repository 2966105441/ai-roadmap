import csv

line = '"张三,医生",13800001111'

print("手写 split：", line.split(","))

with open("test.csv", "w", encoding="utf-8", newline="") as f:
    f.write("姓名,电话\n")
    f.write(line + "\n")

with open("test.csv", encoding="utf-8", newline="") as f:
    for row in csv.reader(f):
        print("csv.reader：", row)
