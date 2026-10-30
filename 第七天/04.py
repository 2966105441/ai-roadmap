with open("../data/text.txt","w",encoding = "utf-8") as f:
    f.write("第一行\n")
    f.write("第二行\n")
with open("../data/text.txt",encoding="utf-8") as f:
    print(f.read())
