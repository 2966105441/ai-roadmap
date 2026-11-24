"""02.py —— 连发 6 句，看发出去的条数到哪不涨了"""
from chat import ChatSession

s = ChatSession("trim_demo.json")
s.reset()

for i in range(1, 7):
    print(f"我：第{i}句")
    print("它：" + s.send(f"第{i}句"))
    print(f"  [本地 {len(s.history)} 条]\n")
