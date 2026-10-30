student = {"name":"张三","age":24,"city":"郑州"}

for k in student:
    print("键：",k)
#注意：直接遍历字典，拿到的是键，不是值。这是和列表不一样的地方——列表遍历拿到元素，字典遍历拿到键。

#三个方法，分别要什么拿什么
student = {"name":"张三","age":24,"city":"郑州"}
print(student.keys())      #所有键
print(student.values())    #所有值
print(student.items())     #所有 键值对


# items：同时拿键和值（最常用）
student = {"name":"张三","age":24,"city":"郑州"}

for k,v in student.items():
    print(f"{k} = {v}")