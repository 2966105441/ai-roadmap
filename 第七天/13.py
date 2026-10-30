def append_line(path,text):
    """在文件末尾追加一行"""
    with open(path,"a",encoding = "utf-8") as f:
        f.write(text+"\n")

append_line("../data/test.txt","新加的一行")

