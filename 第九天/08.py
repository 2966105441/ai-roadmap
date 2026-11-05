try:
    with open("../data/_gbk.txt",encoding = "utf-8") as f:
        f.read()
except UnicodeDecodeError as e:
    raise RuntimeError("读不了这个文件") from e
