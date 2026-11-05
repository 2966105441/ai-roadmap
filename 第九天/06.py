def set_age(age):
    if age < 0:
        raise ValueError(f"年龄不能是负数：{age}")
    return age

try:
    set_age(-5)
except ValueError as e:
    print("抓到：",e)

print("正常：",set_age(20))


def wrapper():
    try:
        int("abc")
    except ValueError:
        print("  记一笔日志，然后继续往上抛")
        raise
try:
    wrapper()
except ValueError as e:
    print(" 最外层接到：",e)

