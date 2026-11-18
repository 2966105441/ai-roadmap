"""03.py —— .env 就是个记事本，load_dotenv 负责抄进去"""
import os

from dotenv import load_dotenv

print("抄之前，LLM_API_KEY =", os.getenv("LLM_API_KEY"))

load_dotenv()          # 这一行，把 第17天/.env 抄进 os.environ

print("抄之后，LLM_API_KEY =", os.getenv("LLM_API_KEY"))
print("模型 =", os.getenv("LLM_MODEL"))
print("超时 =", os.getenv("LLM_TIMEOUT"))
