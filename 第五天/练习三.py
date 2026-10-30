i = 0
count = 0
while i <= 100:
    count += i
    i += 1
print("1+2+3+4+...+100 =",count)


b = 0
while True:
    shuru = input("请输入：")
    if shuru == "q":
        print("输入结束")
        break
    else:
        b += 1
        print("您输入次数：",b)