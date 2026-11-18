def add(name:str,phone:str) -> str:
    return name + phone

print("传对了：",add("张三","138"))
print("传错了：",add(123,456))




def need_int(n:int) -> int:
    return n * 2
print("传int：",need_int(3))
print("传str：",need_int("3"))



def bad(x: 不存在的类型) -> str:
    return "ok"
print(bad(1))