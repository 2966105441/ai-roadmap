import os
DATA = "../data/contacts.txt"
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
# ============ 工具函数区：每个函数只干一件事 ============

def show_menu():
    """打印菜单。不需要函数，也不需要返回值--纯粹的输出"""
    print("=" * 24)
    print("1. 添加联系人")
    print("2. 查找联系人")
    print("3. 查看全部")
    print("4. 删除联系人")
    print("5. 退出")
    print("=" * 24)

def add_contact(contacts):
    """添加。参数是字典本身，改它就行，不需要return"""
    name = input("姓名：")
    if name == "":
        print("姓名不能为空")
        return
    phone = input("电话：")
    if len(phone) != 11:
        print("电话格式不对")
        return
    contacts[name] = phone
    save_contacts(contacts,DATA)
    print(f"已保存：{name}->{phone}")

def find_contact(contacts):
    """查找。注意这里必须 return——因为要告诉调用方"找到了没"""
    name = input("要查谁：")
    if name in contacts:
        print(f"{name}的电话是{contacts[name]}")
        return True
    print(f"没有{name}这个人")
    return False

def show_all(contacts):
    if len(contacts) == 0:
        print("通讯录还是空的，先添加一个吧")
        return
    print(f"共{len(contacts)}位联系人：")
    for name,phone in contacts.items():
        print(f" {name}:{phone}")

def delete_contact(contacts):
    name = input("要删谁：")
    if name in contacts:
        del contacts[name]
        save_contacts(contacts,DATA)
        print(f"已删除{name}")
    else:
        print(f"没有{name}这个人")

#============ 主函数 ===========

def main():
    #contacts = {}
    contacts = load_contacts(DATA)
    while True:
        show_menu()
        choice = input("请选择（1-5）：")

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            find_contact(contacts)
        elif choice == "3":
            show_all(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            print("再见")
            break
        else:
            print("请输入1-5之间的数字")

main()
