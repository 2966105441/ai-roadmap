"""01.py —— 让程序一直跟你说话，直到你说再见"""
count = 0

while True:
    text = input("你：")

    if text == "再见":
        print("它：聊了", count, "句，拜拜")
        break

    count = count + 1
    print("它：你说的是「" + text + "」")
