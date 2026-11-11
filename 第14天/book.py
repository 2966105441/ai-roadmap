import csv
import os


class ContactBook:
    """通讯录：数据和操作数据的方法放在一起"""

    def __init__(self,path):
        self.path = path
        self.contacts = {}    #名字->电话
        self.load()           #建对象的时候就把文件读进来

    #================= 文件读写 ================
    def load(self):
        if not os.path.exists(self.path):
            return
        with open(self.path,encoding = "utf-8-sig",newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                self.contacts[row["姓名"]] = row["电话"]

    def save(self):
        with open(self.path, "w", encoding="utf-8-sig", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=["姓名", "电话"])
            writer.writeheader()
            for name, phone in self.contacts.items():
                writer.writerow({"姓名": name, "电话": phone})

    def add(self,name,phone):
        self.contacts[name] = phone

    def find(self,name):
        return self.contacts.get(name)

    def delete(self,name):
        del self.contacts[name]

    def add(self,name,phone):
        name = name.strip()
        phone = phone.strip()
        if not name:
            raise ContactError("姓名不能为空")
        if not phone.isdigit() or len(phone) != 11:
            raise ContactError(f"电话必须是11位数字，你给的是{phone!r}")
        if name in self.contacts:
            raise ContactError(f"{name} 已经在通讯录里了")
        self.contacts[name] = phone
        self.save()          #改为立马落盘，不会忘

    def __len__(self):
        return len(self.contacts)

    def __contains__(self,name):
        return name in self.contacts

    def __str__(self):
        if not self.contacts:
            return "通讯录是空的"
        lines = [f"共{len(self.contacts)}位联系人："]
        for name,phone in self.contacts.items():
            lines.append(f"  {name} {phone}")
        return "\n".join(lines)


class ContactError(Exception):
    """通讯录专用的异常。所有跟通讯录有关的错误都用它"""
    pass


def main():
    book = ContactBook("../data/contacts.csv")

    while True:
        print("=" * 24)
        print("1.添加   2.查找   3.查看全部   4.删除   5.退出")
        print("=" * 24)
        choice = input("请选择（1-5）：")

        try:
            if choice == "1":
                name = input("姓名：")
                phone = input("电话：")
                book.add(name,phone)
                print(f"已保存：{name}")
            elif choice == "2":
                name = input("要查谁：")
                phone = book.find(name)
                if phone is None:
                    print(f"没有{name}这个人")
                else:
                    print(f"{name}的电话是{phone}")
            elif choice == "3":
                print(book)
            elif choice == "4":
                name = input("要删谁：")
                book.delete(name)
                print(f"已删除{name}")
            elif choice == "5":
                print("再见")
                break
            else:
                print("请输入1-5")
        except ContactError as e:
            print(f"[失败]{e}")

if __name__ == "__main__":
    main()


