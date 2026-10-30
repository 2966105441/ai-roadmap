#练习一
# shu_1 = int(input("输入第一个整数："))
# shu_2 = int(input("输入第二个整数："))
#
# print(f"和：{shu_1 + shu_2}")
# print(f"差：{shu_1 - shu_2}")
# print(f"积：{shu_1 * shu_2}")
# print(f"商：{shu_1 / shu_2:.2f}")

#练习二
# shu_1 = int(input("输入一个整数："))
# if shu_1 % 2 == 0:
#     print("你输入的数是偶数")
# elif shu_1 % 2 != 0:
#     print("你输入的数是奇数")

#练习三
year = int(input("请输入年份："))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("该年是闰年")
else:
    print("该年不是闰年")
