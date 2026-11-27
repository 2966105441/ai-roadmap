"""client.py —— 会话客户端：管历史、存档、自动截断、温度

用法：
    from client import ChatSession
    s = ChatSession("chat.json", temperature=0.7)
    s.send_stream("你好")
"""
import json
import os

import requests

os.environ["NO_PROXY"] = "127.0.0.1,localhost"

URL = "http://127.0.0.1:8000/chat"
URL_STREAM = "http://127.0.0.1:8000/chat_stream"
MAX_MSGS = 7                       # system + 3 轮对话（每轮 2 条）


class ChatSession:
    def __init__(self, file: str, temperature: float = 0.7,
                 system: str = "你是一个简洁的助手。"):
        self.file = file
        self.temperature = temperature
        self.history = [{"role": "system", "content": system}]
        if os.path.exists(file):
            with open(file, encoding="utf-8") as f:
                self.history = json.load(f)
                if self.history and self.history[0].get("role") == "system":
                    self.history[0]["content"] = system  # 存档里的 system 可能过时了
                else:
                    self.history.insert(0, {"role": "system", "content": system})
        if self.history and self.history[0].get("role") == "system":
            self.history[0]["content"] = system      # 存档里的 system 可能过时了
        else:
            self.history.insert(0, {"role": "system", "content": system})

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
        resp = requests.post(URL, json={"messages": self.history,
                                        "temperature": self.temperature}, timeout=10)
        reply = resp.json()["choices"][0]["message"]["content"]
        self.history.append({"role": "assistant", "content": reply})
        self.save()
        return reply

    def send_stream(self, text: str) -> str:
        """边收边打：字到了就 print，收完再存进历史"""
        self.history.append({"role": "user", "content": text})
        self.trim()
        resp = requests.post(URL_STREAM, json={"messages": self.history,
                                               "temperature": self.temperature},
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
