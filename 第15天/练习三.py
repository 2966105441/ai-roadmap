import json
from dataclasses import dataclass, field

RAW = """{
  "id": "chat-001",
  "model": "mi-mo",
  "choices": [
    {"index": 0, "message": {"role": "assistant", "content": "检索增强生成是一种把外部知识喂给模型的方法。"}, "finish_reason": "stop"}
  ],
  "usage": {"prompt_tokens": 42, "completion_tokens": 28, "total_tokens": 70}
}"""

@dataclass
class Usage:
    prompt_tokens: int
    completion_tokens: int
    total_tokens: int

@dataclass
class Message:
    role:str
    content:str

@dataclass
class Choice:
    index: int
    message: Message
    finish_reason: str

@dataclass
class Reply:
    id:str
    model:str
    choices:list[Choice] = field(default_factory=list)
    usage:Usage = None

    @classmethod
    def from_json(cls, raw: str) -> "Reply":
        d = json.loads(raw)
        return cls(
            id=d["id"],
            model=d["model"],
            choices=[Choice(index=c["index"],
                            message=Message(**c["message"]),
                            finish_reason=c["finish_reason"])
                     for c in d["choices"]],
            usage=Usage(**d["usage"]),
        )

r = Reply.from_json(RAW)
print(r.choices[0].message.content)
print(r.usage.total_tokens, "token")
print(type(r.choices[0].message).__name__)