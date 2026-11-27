text = "apple banana apple cherry banana apple"
words = text.split()
cnt = {}
for w in words:
    cnt[w] = cnt.get(w,0) + 1

items = sorted(cnt.items(),key=lambda p:p[1],reverse=True)

for i,(w,n) in enumerate(items,1):
    print(f"{i}.{w}-{n}")