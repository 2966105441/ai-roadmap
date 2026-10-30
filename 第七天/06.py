#坑1：忘了写\n.两行会挤成一行
with open("../data/t2.txt","w",encoding="utf-8") as f:
    f.write("张三，138")
    f.write("李四，139")

with open("../data/t2.txt",encoding = "utf-8") as f:
    print("坑1结果：",repr(f.read()))

#坑2：忘了写"w"，默认是"r"，不能写
try:
    with open("../data/t2.txt",encoding = "utf-8") as f:
        f.write("abc")
except Exception as e:
    print("坑2报错：",e)

# 只要 open()，下一件事就是写 encoding="utf-8"。读要写，写也要写。
# 不写的话，在你机器上：PyCharm 会炸，终端不会炸——这种"换个地方跑就不一样"的 bug 最浪费时间。