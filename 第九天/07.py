class LLMError(Exception):
    """本项目所有大模型相关异常的父类"""
class TimeoutError_(LLMError):
    pass
class RateLimitError_(LLMError):
    pass

def call_model(fail=False):
    if fail == "timeout":
        raise TimeoutError_("等了30秒没响应")
    if fail == "limit":
        raise RateLimitError_("每分钟只能调60次")
    return "模型回答"
for case in [False,"timeout","limit"]:
    try:
        print("  结果：",call_model(case))
    except TimeoutError_ as e:
        print(" 超时了，稍后重试 ->",e)
    except RateLimitError_ as e:
        print("  限流了，等1分钟 ->",e)

try:
    call_model("timeout")
except LLMError as e:
    print("AppError 抓住：",type(e).__name__,e)