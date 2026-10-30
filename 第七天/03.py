from pathlib import Path
BASE = Path(__file__).resolve().parent.parent   #parent = 第七天，再parent = ai-roadmap
p = BASE / "data" / "sample_en.txt"             #用 / 拼路径，比字符串加号干净

with open(p,encoding = "utf-8") as f:
    text = f.read()

print(f"读到{len(text)}个字符")
