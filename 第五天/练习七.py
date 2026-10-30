contacts = {}

while True:
    print("="*20)
    print("1.添加联系人")
    print("2.查找联系人")
    print("3.查看全部")
    print("4.删除联系人")
    print("5.退出")

    choice = input("请选择（1-5）：")

    if choice == "1":
        name = input("姓名：")
        phone = input("电话：")
        contacts[name] = phone
        print(f"已保存：{name}->{phone}")

    elif choice == "2":
        name = input("要查谁：")
        if name in contacts:
            print(f"{name}的电话是{contacts[name]}")
        else:
            print(f"没有{name}这个人")

    elif choice == "3":
        for k,v in contacts.items():
            print(f"{k}->{v}")

    elif choice == "4":
        name = input("请输入需要删除的信息：")
        if name in contacts:
            contacts.pop(name)
            print("该用户删除成功")
        else:
            print("没有该用户信息")
    elif choice == "5":
        print("退出")
        break

    else:
        print("请输入正确的数字（1-5）")
