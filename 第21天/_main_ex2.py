"""练习二答案：读文件 → 取前几行 → 让模型说讲了什么"""
import argparse
import logging

import requests

from config import get_settings

URL = "http://127.0.0.1:8000/chat"


def ask(prompt: str) -> str:
    resp = requests.post(URL, json={"prompt": prompt}, timeout=10)
    resp.raise_for_status()
    return resp.json()["choices"][0]["message"]["content"]


def main() -> None:
    parser = argparse.ArgumentParser(description="读文件并让模型总结")
    parser.add_argument("input", help="文本文件路径")
    parser.add_argument("-n", "--top", type=int, help="取前几行，不写就用配置里的")
    args = parser.parse_args()
    logging.basicConfig(level=logging.INFO, format="%(levelname)s | %(message)s")
    log = logging.getLogger("tool")
    s = get_settings()
    top = args.top if args.top is not None else s.top
    with open(args.input, encoding="utf-8") as f:
        lines = [ln.strip() for ln in f if ln.strip()]
    text = "\n".join(lines[:top])
    log.info("取了 %d 行，共 %d 个字", len(lines[:top]), len(text))
    print(ask("请用一句话总结这段文字：\n" + text))


if __name__ == "__main__":
    main()
