#在列表里，加东西要用 append()，改东西要用索引赋值，是两件事。字典里只有一个动作：给键赋值。键不存在就是加，键已存在就是改，Python 自己判断。

student = {"name":"张三","age":24}
print("初始：",student)

student["score"] = 95              # score 不存在 → 新增
print("加score：",student)

student["age"] = 25                # age 已存在 → 修改
print("改age：",student)

del student["age"]                 # 删除整个键值对
print("删age：",student)


got = student.pop("score")          # 删除并把值还给你（和列表的 pop 一样）
print("pop出来的：",got)
print("最后：",student)