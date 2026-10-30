student = {"name":"胡涛","age":22,"city":"郑州"}
print(student["name"])

student["score"] = 95
print(student)
student["age"] = 25
print(student)
student.pop("city")
print(student)

print(student.get("xingbei","还没输入"))

for key,value in student.items():
    print(f"{key}->{value}")