# i = 1
# while i <= 3:
#     print("第",i,"次")
#     i += 1
# print("循环结束，i =",i)

#while 的条件可以是任何能判断真假的东西
#条件1：数字比较
n = 5
while n > 0:
    print(n,end="")
    n -= 1
print()

#条件2：一个字符串（空字符是假，非空是真）
word = "abc"
count = 0
while word:
    count += 1
    if count == 3:
        word = ""
print("转了",count,"次")


