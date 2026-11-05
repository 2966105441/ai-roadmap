import os

class CounterError(Exception):
    """词频统计器自己的异常基类"""

class EmptyFileError(CounterError):
    """文件读到了，但是空的"""

class WordCounter:
    def __init__(self,path,stop_words=None):
        self.path = path
        self.stop_words = stop_words if stop_words is not None else set()
        self.words = []
        self.count = []

    def load(self):
        if not os.path.exists(self.path):
            raise CounterError(f"文件不存在：{self.path}")
        try:
            with open(self.path,encoding="utf-8") as f:
                text = f.read()
        except UnicodeDecodeError as e:
            raise CounterError(f"文件编码不是UTF-8：{self.path}") from e
        except PermissionError as e:
            raise CounterError(f"没有权限读：{self.path}") from e
        if text.strip() == "":
            raise EmptyFileError(f"文件是空的：{self.path}")
        return text

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

    def top(self,n = 5):
        pairs = [(c,w) for w,c in self.count.items()]
        pairs.sort(reverse=True)
        return [(w,c) for c,w in pairs[:n]]

    def report(self,n=5):
        total = len(self.words)
        print("=" * 36)
        print(f"文件：{self.path}")
        print(f"总词数：{total}    不同词数：{len(self.count)}")
        print("=" * 36)
        for i,(w,c) in enumerate(self.top(n),start = 1):
            pct = c / total if total else 0
            print(f"{i:>2}. {w:<14} {c:>3}  {pct:>6.1%}  {"▮" * c}")

    def run(self, n=5):
        try:
            text = self.load()
            self.clean(text)
            self.count_words()
        except EmptyFileError as e:
            print(f"[跳过] {e}")
            return False
        except CounterError as e:
            print(f"[失败] {e}")
            return False
        else:
            self.report(n)
            return True

STOP = {"the", "a", "an", "is", "are", "and", "or", "to", "of", "in",
            "on", "it", "this", "that", "how", "we", "your", "but", "then"}

print("1) 正常文件")
WordCounter("../data/sample_en.txt", STOP).run(3)

print("2) 文件不存在")
WordCounter("../data/nosuch.txt").run()