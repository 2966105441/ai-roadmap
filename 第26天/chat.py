"""chat.py —— 一个能自己管记忆、管文件的会话类"""
import json
import os

import requests

os.environ["NO_PROXY"] = "127.0.0.1,localhost"

URL = "http://127.0.0.1:8000/chat"


class ChatSession:
    def __init__(self, file: str):
        self.file = file
        self.history = [{"role": "system", "content": "你是一个简洁的助手。"}]
        if os.path.exists(file):
            with open(file, encoding="utf-8") as f:
                self.history = json.load(f)

    def send(self, text: str) -> str:
        self.history.append({"role": "user", "content": text})
        resp = requests.post(URL, json={"messages": self.history}, timeout=10)
        reply = resp.json()["choices"][0]["message"]["content"]
        self.history.append({"role": "assistant", "content": reply})
        with open(self.file, "w", encoding="utf-8") as f:
            json.dump(self.history, f, ensure_ascii=False, indent=2)
        return reply
