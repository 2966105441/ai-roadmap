text = "abc"
try:
    n = int(text)
    print("转换成功：",n)
except ValueError:
    print("转换失败：这不是一个数字")

print("程序继续往下跑")


try:
    n = int("abc")
except ValueError as e:
    print("类型：",type(e).__name__)
    print("原因：",e)