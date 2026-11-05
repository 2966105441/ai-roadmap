class LLMError(Exception):
    """调用大模型失败"""

class ModelTimeoutError(LLMError):
    pass

class RateLimitError(LLMError):
    pass


attempts = {"n": 0}

def fake_call():
    """模拟：前两次超时，第三次成功"""
    attempts["n"] += 1
    if attempts["n"] < 3:
        raise ModelTimeoutError("30 秒没响应")
    return "模型回答：你好"


def call_with_retry(max_tries=3):
    for i in range(1, max_tries + 1):
        try:
            result = fake_call()
        except RateLimitError as e:
            print(f"  第{i}次：被限流（{e}），重试没用")
            return None
        except ModelTimeoutError as e:
            print(f"  第{i}次：超时（{e}）")
            if i == max_tries:
                print("  重试次数用完，放弃")
                return None
        else:
            print(f"  第{i}次：成功")
            return result
        finally:
            print(f"  第{i}次调用结束")


print("开始调用：")
r = call_with_retry(3)
print("最终结果：", r)