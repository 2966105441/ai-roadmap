"""02.py —— logging 有五个级别，默认只给你看三条"""
import logging

logging.debug("debug：最啰嗦，开发时看")
logging.info("info：正常流程，比如「读到 249 个字」")
logging.warning("warning：不对劲，但还能继续")
logging.error("error：这一步失败了")
logging.critical("critical：整个程序要完")

print()
print("root 当前的级别 =", logging.getLevelName(logging.getLogger().level), flush=True)


# DEBUG	10 · 最啰嗦。变量值、循环第几次、算了多久。只在自己调代码时看
# INFO	20 · 正常流程。「读到 249 个字」「切出 10 个词」「请求成功」。上线后要留的就是这一档
# WARNING	30 · 不对劲但还能继续。「停用词文件是空的，这次没过滤」
# ERROR	40 · 这一步失败了。「文件写不进去」「接口返回 500」
# CRITICAL	50 · 整个程序要完。用得少，ERROR 一般够了