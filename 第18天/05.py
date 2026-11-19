"""05.py —— 和 01.py 干同一件事，只是换成了日志"""
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s | %(levelname)-7s | %(name)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
log = logging.getLogger("wordstat")

文本 = "检索 是 大模型 的 关键 检索 能 提升 回答 质量"
log.debug("文本长度 = %s", len(文本))

词表 = 文本.split()
log.info("切出 %s 个词", len(词表))
log.debug("文本长度 = %s", len(文本))

统计 = {}
for w in 词表:
    统计[w] = 统计.get(w, 0) + 1

log.info("不同词 %s 个", len(统计))
log.warning("没过滤停用词，结果偏大")
log.info("出现最多的是 %s", max(统计, key=统计.get))
