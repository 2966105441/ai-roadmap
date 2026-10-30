#字符串：改不了
# s = "abc"
# s[0] = "x"

#列表：能改
fruits = ["苹果","香蕉"]
fruits[0] = "红苹果"
print(fruits)
#字符串是刻在石头上的，列表是写在白板上的。这两种东西在程序里叫"不可变"和"可变"，后面会反复提到。

fruits.append("西瓜")
fruits.insert(1,"西瓜")
fruits.remove("香蕉")
fruits.pop()
fruits[0] = "红苹果"
print(fruits)