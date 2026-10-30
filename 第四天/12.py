# range：不想遍历列表，只想跑 N 次
# 如果我只是想"重复 5 次"，没有列表怎么办？用 range()，它直接生成一串数字。

for i in range(3):
    print("i =",i)

print("-"*5)
for i in range(1,4):
    print("1到3：",i)

print("-"*5)

for i in range(0,10,3):
    print("步长3：",i)

# range(3)	        0, 1, 2	      从 0 开始，不含 3
# range(1, 4)	    1, 2, 3	      含头不含尾，还是这个规则
# range(0, 10, 3)	0, 3, 6, 9	  第三个参数是步长