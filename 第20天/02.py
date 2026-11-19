"""02.py —— 同样的需求，argparse 三行搞定，还自带 -h 帮助"""
import argparse

parser = argparse.ArgumentParser(description="数一数文件里有多少字")
parser.add_argument("input", help="要读的文件路径")
args = parser.parse_args()

print("input =", args.input)
with open(args.input, encoding="utf-8") as f:
    print("读了", len(f.read()), "个字")
