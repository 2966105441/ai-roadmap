"""config.py —— 所有配置都在这里读一次，别的文件只管 import"""
import os

from dotenv import load_dotenv

load_dotenv()                                     # ① 把 .env 抄进环境变量

BASE_URL = os.getenv("LLM_BASE_URL")              # ② 一项一行，一眼看清
API_KEY = os.getenv("LLM_API_KEY")
MODEL = os.getenv("LLM_MODEL", "fake-mimo")       # ③ 第二个参数是默认值
TIMEOUT = float(os.getenv("LLM_TIMEOUT", "10"))   # ④ 数字要自己转
MAX_TOKENS = int(os.getenv("LLM_MAX_TOKENS", "512"))


if not API_KEY:                                   # ⑤ 缺了就当场停
    raise SystemExit("缺少 LLM_API_KEY，去 .env 里补上")


if __name__ == "__main__":                        # 直接 Run 这个文件时才打印
    print("BASE_URL =", BASE_URL)
    print("API_KEY  =", API_KEY[:5] + "******")
    print("MODEL    =", MODEL)
    print("TIMEOUT  =", TIMEOUT, "| 类型 =", type(TIMEOUT).__name__)
    print("MAX_TOKENS =", MAX_TOKENS, "| 类型 =", type(MAX_TOKENS).__name__)

