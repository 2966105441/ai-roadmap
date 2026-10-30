#一个更隐蔽的坑：b = a 不是复制
a = [1,2,3]
b = a
b.append(4)
print("a =",a)
print("b =",b)

c = a[:]
c.append(99)
print("a =",a)
print("c =",c)
