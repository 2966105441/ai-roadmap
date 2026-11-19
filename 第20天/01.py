"""01.py —— 以前想换文件，只能改代码；用 sys.argv 能改，但很啰嗦"""
import sys

print("收到的全部参数 =", sys.argv)

# 第 0 个永远是脚本自己的名字，所以真正的内容从第 1 个开始
if len(sys.argv) < 2:
    print("你没给文件名。正确用法：01.py ../data/sample_zh.txt")
    raise SystemExit(1)

文件名 = sys.argv[1]
with open(文件名, encoding="utf-8") as f:
    text = f.read()
print("读了", len(text), "个字")
