fruits = ["苹果", "香蕉", "橙子"]
print("初始：", fruits)

fruits.append("葡萄")          # 末尾加
print("append 后：", fruits)

fruits.insert(1, "西瓜")       # 插到编号 1 的位置
print("insert 后：", fruits)

fruits.remove("香蕉")          # 按内容删
print("remove 后：", fruits)

gone = fruits.pop()              # 弹出最后一个，并接住它
print("被弹出的：", gone)
print("pop 后：", fruits)

fruits[0] = "红苹果"          # 直接改
print("改完：", fruits)