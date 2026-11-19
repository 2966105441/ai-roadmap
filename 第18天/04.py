"""04.py —— 日志写进文件，一行就够了"""
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)-7s | %(message)s",
    datefmt="%H:%M:%S",
    filename="app.log",
    filemode="w",
    encoding="utf-8",
)

logging.info("这行去哪了？控制台上看不到我")
logging.warning("中文日志：检索到 82 个词")

print("=== app.log 里的内容 ===")
print(open("app.log", encoding="utf-8").read())
