#先用w写两行
with open("../data/text.txt","w",encoding="utf-8") as f:
    f.write("A\n")
    f.write("B\n")

#再用a追加
with open("../data/text.txt","a",encoding = "utf-8") as f:
    f.write("C(追加的)\n")

with open("../data/text.txt",encoding = "utf-8") as f:
    print("---用a之后---")
    print(f.read())

#故意用w再打开一次
with open("../data/text.txt","w",encoding = "utf-8") as f:
    f.write("D(新的开始)\n")

with open("../data/text.txt",encoding="utf-8") as f:
    print("---用w之后---")
    print(f.read())