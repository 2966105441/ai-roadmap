class Swallow:
    def __enter__(self):
        return self

    def __exit__(self,exc_type,exc_val,tb):
        print("  我把异常吃了，返回True")
        return True

with Swallow():
    raise ValueError("这条应该消失")

print("  程序继续跑，没人知道刚才出过错")

    