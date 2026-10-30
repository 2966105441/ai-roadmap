with open("../data/sample_zh.txt",encoding="utf-8") as f:
    text = f.read()

print(f"总字符串：{len(text)}")

count = {}
for ch in text:
    if ch in "。，\n":
        continue
    count[ch] = count.get(ch,0)+1
print(f"不同字数：{len(count)}")

pairs = []
for ch,c in count.items():
    pairs.append((c,ch))
pairs.sort(reverse=True)

print("Top 15 字：")
for c,ch in pairs[:15]:
    print(f"  {ch} {c}")