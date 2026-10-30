#*args 就是"把多出来的位置参数全收下，打包成元组"：
def total(*nums):                # 星号在参数名前面
    print(f"收到：{nums}")
    return sum(nums)

print(total(1, 2, 3))
print(total(1, 2, 3, 4, 5))
print(total())

#  **kwargs 是"把多出来的关键字参数全收下，打包成字典"：
def create_message(**info):       # 两个星号
    print(f"收到：{info}")
    return info

print(create_message(role="user", content="你好"))
create_message(role="system", content="你是助手", priority=1)
