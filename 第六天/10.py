# 关键字参数：参数一多，就该用它
# 约 8 分钟 · 这决定了你以后看 API 文档能不能看懂
# 调用函数时，可以用参数名指定传哪个值，这样顺序就无所谓了：

def greet(name,greeting="你好"):
    print(f"{greeting},{name}")

greet("李四")                    # 位置参数
greet(name="李四")              # 关键字参数
greet(greeting="晚上好",name="王五")    # 顺序反了也行



#什么时候用？参数超过 3 个的时候。理由很实际——没人记得住第 4 个位置该放什么。你以后一定会写这种代码：
# response = client.chat(
#     model = "glm-4",
#     messages=messages,
#     temperature=0.7,
#     max_tokens=1024,
# )
# 自己写的函数：参数 ≤ 3 个用位置，> 3 个建议全用关键字。
# 调用别人的函数：拿不准就全用关键字，最保险。多打几个字，省掉半小时排错。
