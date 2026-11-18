"""02.py —— 自己往里塞一个，就能塞"""
import os

os.environ["MY_NAME"] = "小明"
print("刚塞的：", os.getenv("MY_NAME"))

os.environ["MY_NAME"] = "小红"
print("改掉后：", os.getenv("MY_NAME"))

del os.environ["MY_NAME"]
print("删掉后：", os.getenv("MY_NAME"))

print("\n但用方括号取值，取不到会报错：")
try:
    print(os.environ["MY_NAME"])
except KeyError as e:
    print("  KeyError:", e)
