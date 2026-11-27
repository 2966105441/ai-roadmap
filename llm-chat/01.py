"""01.py —— 同一句话，两个 system，各问一次"""
import os

import requests

os.environ["NO_PROXY"] = "127.0.0.1,localhost"
HERE = os.path.dirname(os.path.abspath(__file__))
QUESTIONS = ["今天郑州天气怎么样", "列表怎么去重"]

for role in ["vague", "tutor"]:
    with open(os.path.join(HERE, "prompts", role + ".txt"), encoding="utf-8") as f:
        system = f.read()
    print(f"===== {role}.txt =====")
    for q in QUESTIONS:
        resp = requests.post("http://127.0.0.1:8000/chat", json={
            "messages": [{"role": "system", "content": system},
                         {"role": "user", "content": q}],
        }, timeout=10)
        reply = resp.json()["choices"][0]["message"]["content"]
        print(f"问：{q}")
        print(f"答：{reply}")
    print()
