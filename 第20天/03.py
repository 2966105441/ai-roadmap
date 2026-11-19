"""03.py —— 可选参数：不给就用默认值，给了就按你的来"""
import argparse

parser = argparse.ArgumentParser(description="数一数文件里有多少字")
parser.add_argument("input", help="要读的文件路径")
parser.add_argument("-n", "--top", type=int, default=5, help="显示前几名，默认 5")
args = parser.parse_args()

print("input =", args.input)
print("top   =", args.top, "（类型是", type(args.top).__name__, "）")
