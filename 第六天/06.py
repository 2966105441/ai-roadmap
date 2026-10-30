def check(score):
    if score >= 60:
        return "及格"
        print("这句话永远不会被打印")  #到不了这行
    return "不及格"

print(check(85))
print(check(59))

# 所以 return 可以当 break 用，而且更彻底——break 只跳出循环，return 直接结束整个函数。\


def get_phone(contacts,name):
    if name == "":
        return "名字不能为空"
    if name not in contacts:
        return f"没有{name}这个人"
    return contacts[name]

print(get_phone({"张三":"138"},"张三"))
print(get_phone({"张三":"138"},"王五"))
print(get_phone({"张三":"138"},""))
