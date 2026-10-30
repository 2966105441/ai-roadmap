with open("../data/sample_zh.txt", encoding="utf-8") as f:
    text = f.read()

sents = []
for s in text.replace("。", "|").replace("\n", "|").split("|"):
    if s.strip() != "":
        sents.append(s.strip())

print(f"切出 {len(sents)} 句")
for i, s in enumerate(sents[:4], start=1):
    print(f"  {i}. {s}")