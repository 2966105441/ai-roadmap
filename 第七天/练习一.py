def find_word(text,word):
    """统计某个词出现的次数，不区分大小写"""
    target = word.lower()
    n = 0
    for w in text.lower().split():
        w = w.strip(".,!?")
        if w == target:
            n += 1
    return n

with open("../data/sample_en.txt",encoding="utf-8") as f:
    t = f.read()

print(find_word(t,"Retrieval"))
