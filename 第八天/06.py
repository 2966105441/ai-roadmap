class WordCounter:
    """词频统计器:数据(路径/词表/统计结果)和方法（读/洗/数/排）装在一起"""
    def __init__(self,path,stop_words=None):
        self.path = path
        if stop_words is None:
            self.stop_words = stop_words
        else:
            self.stop_words = stop_words
        self.words = []             #洗好的词
        self.count = {}             #{词：次数}

    def load(self):
        with open(self.path,encoding="utf-8") as f:
            return f.read()

    def clean(self,text):
        result = []
        for w in text.lower().split():
            w = w.strip(".,!?;:\"'()")
            if w == "" or w in self.stop_words:
                continue
            result.append(w)
        self.words = result
        return result

    def count_words(self):
        c = {}
        for w in self.words:
            c[w] = c.get(w,0) + 1
        self.count = c
        return c

    def top(self, n=5):
        pairs = []
        for w, c in self.count.items():
            pairs.append((c, w))  # 次数放前面，排序就按次数
        pairs.sort(reverse=True)
        return [(w, c) for c, w in pairs[:n]]

    def report(self, n=5):
        total = len(self.words)
        print("=" * 36)
        print(f"文件：{self.path}")
        print(f"总词数：{total}   不同词数：{len(self.count)}")
        print("=" * 36)
        for i, (w, c) in enumerate(self.top(n), start=1):
            pct = c / total if total else 0
            print(f"{i:>2}. {w:<14} {c:>3}  {pct:>6.1%}  {'▮' * c}")

    def run(self, n=5):
        """一键跑完四步"""
        self.clean(self.load())
        self.count_words()
        self.report(n)


STOP = {"the", "a", "an", "is", "are", "and", "or", "to", "of", "in", "on", "it",
        "this", "that", "how", "we", "your", "but", "then", "do", "does", "can",
        "not", "be", "with", "why", "most", "often", "first", "right", "good",
        "alone", "what", "them"}

c1 = WordCounter("../data/sample_en.txt", STOP)
c1.run(5)

print()
c2 = WordCounter("../data/sample_zh.txt")
c2.run(3)