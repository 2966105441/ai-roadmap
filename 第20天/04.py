"""04.py —— 开关型参数：写了就是 True，没写就是 False"""
import argparse

parser = argparse.ArgumentParser(description="看文件里有几行")
parser.add_argument("input", help="要读的文件路径")
parser.add_argument("--verbose", action="store_true", help="把每一行也打印出来")
args = parser.parse_args()

with open(args.input, encoding="utf-8") as f:
    lines = [ln.strip() for ln in f if ln.strip()]

print("一共", len(lines), "行")
print("verbose =", args.verbose)

if args.verbose:
    for i, ln in enumerate(lines, 1):
        print(f"  {i}. {ln[:30]}")
