"""03.py —— 不用手剥，让 pydantic 接住整坨 JSON"""
import os

import requests
from pydantic import BaseModel

os.environ["NO_PROXY"] = "127.0.0.1,localhost"

class Message(BaseModel):
    role: str
    content: str

class Choice(BaseModel):
    message: Message

class ChatReply(BaseModel):
    model: str
    choices: list[Choice]

resp = requests.post("http://127.0.0.1:8000/chat", json={"prompt": "什么是 RAG"}, timeout=5)
reply = ChatReply(**resp.json())

print("模型：", reply.model)
print("回复：", reply.choices[0].message.content)
