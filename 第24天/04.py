"""04.py —— 结构升级：从裸列表变成会话对象"""
import json
from datetime import datetime

from pydantic import BaseModel


class Message(BaseModel):
    role: str
    content: str


class Session(BaseModel):
    updated_at: str
    messages: list[Message]


with open("chat.json", encoding="utf-8") as f:
    old = json.load(f)
s = Session(updated_at=datetime.now().strftime("%Y-%m-%d %H:%M"), messages=old)
with open("chat2.json", "w", encoding="utf-8") as f:
    json.dump(s.model_dump(), f, ensure_ascii=False, indent=2)
print("更新", s.updated_at, "| 共", len(s.messages), "条")
print("末条：", s.messages[-1].role, "|", s.messages[-1].content)
