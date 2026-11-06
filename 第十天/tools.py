def greet(name):
    return f"你好,{name}"

def add(a,b):
    return a+b

print(">>> tools.py的顶层代码被执行了")

if __name__ == "__main__":
    print("测试greet：",greet("小明"))
    print("测试add：",add(1,2))