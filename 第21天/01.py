"""01.py —— 全塞一个文件：能跑，但下一个脚本还得抄一遍"""
import argparse
import logging
import os

from dotenv import load_dotenv

load_dotenv()
logging.basicConfig(level=logging.INFO, format="%(levelname)s | %(message)s")
log = logging.getLogger("tool")
log.info("模型 = %s", os.getenv("LLM_MODEL"))

parser = argparse.ArgumentParser(description="看文件里有几行")
parser.add_argument("input", help="文本文件路径")
parser.add_argument("-n", "--top", type=int, default=3, help="打印前几行")
args = parser.parse_args()

with open(args.input, encoding="utf-8") as f:
    lines = [ln.strip() for ln in f if ln.strip()]

log.info("读到 %d 行", len(lines))
print("最长的一行：", max(lines, key=len)[:30])
for i, ln in enumerate(lines[:args.top], 1):
    print(f"{i}. {ln[:24]}")
