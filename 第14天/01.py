import csv

#1.把老的txt读进字典
old = {}
with open("../data/contacts.txt",encoding = "utf-8") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        parts = line.split(",")
        if len(parts) == 2:
            old[parts[0]] = parts[1]

print(f"读到{len(old)}条")

#2.写到正式的CSV（带表头）
with open("../data/contacts.csv","w",encoding="utf-8-sig",newline="") as f:
    writer = csv.DictWriter(f,fieldnames=["姓名","电话"])
    writer.writeheader()
    for name,phone in old.items():
        writer.writerow({"姓名":name,"电话":phone})

print("迁移完成，看 ../data/contacts.csv")