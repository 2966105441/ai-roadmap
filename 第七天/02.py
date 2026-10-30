#方式一：read() -- 一次全读成一个长字符串
with open("../data/sample_en.txt",encoding="utf-8") as f:
    text = f.read()
print("方式1：字符数",len(text))

#方式二：readlines() -- 读成列表，每行一个元素（带/n）
with open("../data/sample_en.txt",encoding="utf-8") as f:
    lines = f.readlines()
print("方式二：行数",len(lines))
print("方式二：第一行",repr(lines[0]))

#方式三:for line in f -- 逐行读，最省内存
with open("../data/sample_en.txt",encoding = "utf-8") as f:
    n = 0
    for line in f:
        n += 1
print("方式三：行数",n)