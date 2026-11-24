"""chat.py —— 一个能自己管记忆、管文件的会话类（Day 029 加了自动截断）"""
import json
import os

import requests

os.environ["NO_PROXY"] = "127.0.0.1,localhost"

URL = "http://127.0.0.1:8000/chat"
URL_STREAM = "http://127.0.0.1:8000/chat_stream"
MAX_MSGS = 7                       # system + 3 轮对话（每轮 2 条）


class ChatSession:
    def __init__(self, file: str):
        self.file = file
        self.history = [{"role": "system", "content": "你是一个简洁的助手。"}]
        if os.path.exists(file):
            with open(file, encoding="utf-8") as f:
                self.history = json.load(f)

    def trim(self) -> None:
        """太长了就删掉最早的一问一答，system 永远保住"""
        while len(self.history) > MAX_MSGS:
            del self.history[1:3]


    def save(self) -> None:
        with open(self.file, "w", encoding="utf-8") as f:
            json.dump(self.history, f, ensure_ascii=False, indent=2)

    def reset(self) -> None:
        del self.history[1:]
        self.save()

    def trim(self) -> None:
        """太长了就删掉最早的一问一答，system 永远保住"""
        while len(self.history) > MAX_MSGS:
            del self.history[1:3]

    def send(self, text: str) -> str:
        self.history.append({"role": "user", "content": text})
        self.trim()
        resp = requests.post(URL, json={"messages": self.history}, timeout=10)
        reply = resp.json()["choices"][0]["message"]["content"]
        self.history.append({"role": "assistant", "content": reply})
        self.save()
        return reply

    def send_stream(self, text: str) -> str:
        """边收边打：字到了就 print，收完再存进历史"""
        self.history.append({"role": "user", "content": text})
        self.trim()
        resp = requests.post(URL_STREAM, json={"messages": self.history},
                             stream=True, timeout=10)
        parts = []
        for line in resp.iter_lines(decode_unicode=True):
            if not line or not line.startswith("data: "):
                continue
            data = line[6:]
            if data == "[DONE]":
                break
            piece = json.loads(data)["choices"][0]["delta"]["content"]
            print(piece, end="", flush=True)
            parts.append(piece)
        reply = "".join(parts)
        self.history.append({"role": "assistant", "content": reply})
        self.trim()
        self.save()
        return reply
