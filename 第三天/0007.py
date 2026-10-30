# 写法	读作	 什么时候是 True
# and	并且	 两边都为真才行
# or	或者	 有一边为真就行
# not	取反	 把 True 变 False，False 变 True

age = 20
score = 85
print(age >= 18 and score >= 60)
print(age >= 18 or score >= 90)
print(not age >= 18)