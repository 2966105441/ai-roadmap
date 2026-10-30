#break 和 continue：半路退出与跳过
n = 1
while True:
    print("检测",n)
    if n == 3:
        print("找到了，跳出")
        break
    n += 1

print("循环外n =",n)