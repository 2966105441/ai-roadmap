"""main.py —— 入口：参数、日志、配置各就各位"""
import argparse
import logging

from config import get_settings


def main() -> None:
    parser = argparse.ArgumentParser(description="看文件里有几行")
    parser.add_argument("input", help="文本文件路径")
    parser.add_argument("-n", "--top", type=int, help="打印前几行，不写就用配置里的")
    args = parser.parse_args()
    logging.basicConfig(level=logging.INFO, format="%(levelname)s | %(message)s")
    log = logging.getLogger("tool")
    s = get_settings()
    top = args.top if args.top is not None else s.top
    log.info("模型 = %s，准备打印 %d 行", s.model, top)
    with open(args.input, encoding="utf-8") as f:
        lines = [ln.strip() for ln in f if ln.strip()]
    for i, ln in enumerate(lines[:top], 1):
        print(f"{i}. {ln[:24]}")

 
if __name__ == "__main__":
    main()
