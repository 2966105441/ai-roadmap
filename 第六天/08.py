def greet(name,greeting="你好"):    #greeting 有默认值
    print(f"{greeting},{name}")

greet("张三")                           #不传第二个-》用默认值"你好”
greet("张三","早上好")     #传了->覆盖默认值

# 有默认值的参数必须放在没默认值的后面。写成 def f(a=1, b): 会直接报错：
# SyntaxError: parameter without a default follows parameter with a default
# 人话：「你把一个没有默认值的参数，放在了有默认值的参数后面」。