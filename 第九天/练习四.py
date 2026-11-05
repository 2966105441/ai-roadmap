def f():
    try:
        return "返回值"
    finally:
        print("  finally一定先执行，再返回")

print("  函数返回：",f())