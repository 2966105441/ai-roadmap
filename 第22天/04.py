"""04.py —— 包成 ask()，超时和断线都变成一句人话"""
import os

import requests

os.environ["NO_PROXY"] = "127.0.0.1,localhost"
URL = "http://127.0.0.1:8000/chat"


def ask(prompt: str) -> str:
    try:
        resp = requests.post(URL, json={"prompt": prompt}, timeout=10)
        resp.raise_for_status()
    except requests.Timeout:
        return "（超时了，等会儿再试）"
    except requests.ConnectionError:
        return "（连不上，fake_api.py 开了吗）"
    return resp.json()["choices"][0]["message"]["content"]


if __name__ == "__main__":
    for q in ["什么是 RAG", "它解决什么问题"]:
        print("问：", q)
        print("答：", ask(q))
        print()
