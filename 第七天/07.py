import os

def load_contacts(path):
    """从文件读通讯录，返回字典。文件不存在就返回空字典"""
    contacts = {}
    if not os.path.exists(path):      #文件还不存在，很正常
        return contacts
    with open(path,encoding = "utf-8") as f:
        for line in f:
            line = line.strip()
            if line == "":
                continue
            parts = line.split(",")
            if len(parts) != 2:
                continue
            name = parts[0]
            phone = parts[1]
            contacts[name] = phone
    return contacts

def save_contacts(contacts, path):
    """把字典写回文件，整份覆盖"""
    with open(path, "w", encoding="utf-8") as f:
        for name, phone in contacts.items():
            f.write(f"{name},{phone}\n")     # 一定要带 \n


#====== 测试 ======
DATA = "../data/contacts.txt"

print("第一次运行：")
c = load_contacts(DATA)
print("  读到：",c)
c["张三"] = "13800001111"
c["李四"] = "13900002222"
save_contacts(c,DATA)
print("  写到文件：")
with open(DATA,encoding="utf-8") as f:
    print(" "+f.read().replace("\n","\n ").rstrip())

print()
print("模拟重启程序")
c2 = load_contacts(DATA)
print("  读到：",c2)
c2 = load_contacts(DATA)
print("  读到：",c2)
c2["王五"] = "13700003333"
save_contacts(c2,DATA)
print("  再加一个后：",load_contacts(DATA))
