"""03.py —— 一行 basicConfig，改级别 + 加时间"""
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s | %(levelname)-7s | %(message)s",
    datefmt="%H:%M:%S",
)

logging.debug("开始读文件")
logging.info("读到 249 个字")
logging.warning("停用词文件是空的")
logging.error("写结果失败")

print("\n注意：DEBUG 也出来了，因为 level 改成了 DEBUG", flush=True)
