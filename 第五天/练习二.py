text = "AI 是 未来 AI 改变 世界 AI"
text.split()

count = {}
for word in text.split():
    if word in count:
        count[word] += 1
    else:
        count[word] = 1
print(count)

for w,c in count.items():
    print(f"{w}出现了{c}次")