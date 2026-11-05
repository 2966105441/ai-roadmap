def buggy():
    s = "abc"
    try:
        print(s.length)
    except:
        print("出错了，但我不知道是什么错")
buggy()

#正确做法一
def safe_div(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        print("不能除以0")
        return None
    except TypeError:
        print("参数类型不对")
        return None
print(safe_div(10,2))
print(safe_div(10,0))
print(safe_div(10,"x"))
#正确方法二：
def to_int(s):
    try:
        return int(s)
    except (ValueError, TypeError) as e:
        print("失败了：",type(e).__name__)
        return None

print(to_int("42"),to_int("abc"),to_int(None))