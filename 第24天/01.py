"""01.py —— 把一段对话存成 JSON 文件"""
import json

messages = [
    {"role": "system", "content": "你是一个只回答一句话的助手。"},
    {"role": "user", "content": "什么是检索增强"},
    {"role": "assistant", "content": "先查资料，再回答。"},
]

with open("chat.json", "w", encoding="utf-8") as f:
    json.dump(messages, f, ensure_ascii=False, indent=2)

print("已写入 chat.json，文件内容是：")
with open("chat.json", encoding="utf-8") as f:
    print(f.read())
