"""04.py —— 读出来全是字符串，今天唯一要小心的地方"""
import os

from dotenv import load_dotenv

load_dotenv()

超时 = os.getenv("LLM_TIMEOUT")
print("超时 =", 超时, "| 类型 =", type(超时).__name__)

print("\n直接拿去做数学：")
try:
    print(" ", 超时 + 1)
except TypeError as e:
    print("  TypeError:", e)

print("\n先转成数字再用：")
print("  float(超时) + 1 =", float(超时) + 1)
