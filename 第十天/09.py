import os
import jieba

jieba.add_word("检索增强生成")
jieba.add_word("大语言模型")
jieba.add_word("提示词")

class CounterError(Exception):
    """词频统计器自己的异常基类"""


class EmptyFileError(CounterError):
    """文件读到了，但是空的"""

class WordCounter:
    def __init__(self,path,lang="en",stop_words=None):
        self.path = path
        self.lang = lang
        self.stop_words = stop_words if stop_words is not None else set()
        self.words = []
        self.count = {}
    def load(self):
        if not os.path.exists(self.path):
            raise CounterError(f"文件不存在：{self.path}")
        try:
            with open(self.path,encoding="utf-8") as f:
                text = f.read()
        except UnicodeDecodeError as e:
            raise CounterError(f"文件编码不是UTF-8：{self.path}") from e
        if text.strip() == "":
            raise EmptyFileError(f"文件是空的：{self.path}")
        return text

    def split(self,text):
        if self.lang == "zh":
            raw = jieba.lcut(text)
        else:
            raw = text.lower().split()

        result = []
        for w in raw:
            w = w.strip(".,!?;:\"'()。，！？；：“”’‘（）")
            if w.strip() == "" or w in self.stop_words:
                continue
            result.append(w)
        return result

    def count_words(self):
        c = {}
        for w in self.words:
            c[w] = c.get(w,0) + 1
        self.count = c
        return c

    def top(self,n = 5):
        pairs = [(c,w)for w,c in self.count.items()]
        pairs.sort(reverse=True)
        return [(w,c) for c,w in pairs[:n]]

    def report(self, n=5):
        total = len(self.words)
        print("=" * 36)
        print(f"文件：{self.path}（{self.lang}）")
        print(f"总词数：{total}    不同词数：{len(self.count)}")
        print("=" * 36)
        for i, (w, c) in enumerate(self.top(n), start=1):
            pct = c / total if total else 0
            print(f"{i:>2}. {w:<10} {c:>3}  {pct:>6.1%}")

    def run(self, n=5):
        try:
            text = self.load()
            self.words = self.split(text)
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

ZH_STOP = {"的", "了", "是", "在", "和", "也", "就", "都", "而", "这", "那",
           "它", "我们", "你", "我", "可以", "吗", "呢", "把", "被", "为", "对",
           "从", "到", "并", "先", "然后", "因为", "所以", "但是", "一条"}

if __name__ == "__main__":
    print("1) 中文文件")
    WordCounter("../data/sample_zh.txt", lang="zh", stop_words=ZH_STOP).run(10)

    print()
    print("2) 同一个文件，用英文模式跑")
    WordCounter("../data/sample_zh.txt", lang="en").run(3)