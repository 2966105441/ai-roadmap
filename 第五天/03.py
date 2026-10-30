student = {"name":"张三","age":24,"city":"郑州"}
print(student)
print(student["name"])
print(student["age"])
print(len(student))

# 键必须加引号	{"name": ...} 对，{name: ...} 错——除非你有一个变量恰好叫 name
# 键必须唯一	写两个 "a" 不会报错，但后面的会覆盖前面的，等于白写一个
# 键必须是"不可变"的	字符串、数字、元组可以；列表不行（会报 unhashable，详见报错表）
# 值可以是任何东西	数字、字符串、列表、甚至另一个字典——最后这个后面会用
# 顺序不重要	字典不是靠位置找的，所以别指望"第几个"有意义

student = {"name":"张三","age":24}
print(student["name"])
#print(student[0])    错！字典没有"第0个”
# 列表能 fruits[0]，因为列表有位置。字典没有位置，只能用键。
# 新手第一个错误就是对着字典写 student[0]，然后收到 KeyError: 0——意思是"你没有叫 0 的键"。

student = {"name":"张三"}
#print(student["score"])  取一个不存在的键会报错

student = {"name":"张三","city":"郑州"}
print(student.get("name"))          # 有：正常返回
print(student.get("score"))         # 没有：返回 None
print(student.get("score",0))       # 没有：返回你指定的 0
print(student.get("city","未知"))    # 有：默认值用不上
