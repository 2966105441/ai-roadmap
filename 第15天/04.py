import time

def 报时(func):
    def wrapper(*args,**kwargs):
        print(f"  >>>跑{func.__name__}")
        t = time.time()
        r = func(*args,**kwargs)
        print(f"  <<< 用了{time.time()-t:.4f}秒")
        return r
    return wrapper

def 慢函数(n):
    s = 0
    for i in range(n):
        s += i
    return s

print("===A完全不装饰===")
print("  返回值：",慢函数(100000))

print("===B 手动包一层（这才是@的真身）===")
包好的 = 报时(慢函数)
print("  返回值：",包好的(100000))



print("===C 用@语法（跟B完全等价）===")
@报时
def 慢函数2(n):
    s = 0
    for i in range(n):
        s += i
    return s

print("  放回值:",慢函数2(100000))


print("慢函数2.__name__ =",慢函数2.__name__)



import functools

def 报时3(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        return func(*args,**kwargs)
    return wrapper

@报时3
def 慢函数3(n):
    return n

print("慢函数3.__name__ =",慢函数3.__name__)