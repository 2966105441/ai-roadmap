import os
import json
import jieba

jieba.add_word("检索增强生成")
jieba.add_word("大语言模型")
jieba.add_word("提示词")

DEFAULT_CONFIG = {
    "default_lang": "en",
    "top_n": 3,
    "stop_words_file": None,
    "show_pct": True,
}


class CounterError(Exception):
    """词频统计器自己的异常基类"""


class EmptyFileError(CounterError):
    """文件读到了，但是空的"""


class ConfigError(CounterError):
    """配置文件有问题"""


def load_config(path="config.json"):
    """读配置文件；文件不在就用默认值"""
    if not os.path.exists(path):
        print(f"[提示] 没找到配置文件 {path}，用默认配置")
        return DEFAULT_CONFIG.copy()

    try:
        with open(path, encoding="utf-8") as f:
            cfg = json.load(f)
    except json.JSONDecodeError as e:
        raise ConfigError(
            f"config.json 第 {e.lineno} 行第 {e.colno} 列写错了：{e.msg}"
        ) from e

    for k, v in DEFAULT_CONFIG.items():
        cfg.setdefault(k, v)
    return cfg


def load_stop_words(path):
    """一行一个词；空行和 # 注释跳过"""
    if not path:
        return set()
    if not os.path.exists(path):
        print(f"[提示] 停用词表不存在：{path}，本次不过滤")
        return set()

    words = set()
    with open(path, encoding="utf-8") as f:
        for line in f:
            w = line.strip()
            if w == "" or w.startswith("#"):
                continue
            words.add(w)
    return words


class WordCounter:
    def __init__(self, path, lang="en", stop_words=None, show_pct=True):
        self.path = path
        self.lang = lang
        self.stop_words = stop_words if stop_words is not None else set()
        self.show_pct = show_pct
        self.words = []
        self.count = {}

    def load(self):
        if not os.path.exists(self.path):
            raise CounterError(f"文件不存在：{self.path}")
        try:
            with open(self.path, encoding="utf-8") as f:
                text = f.read()
        except UnicodeDecodeError as e:
            raise CounterError(f"文件编码不是 UTF-8：{self.path}") from e
        if text.strip() == "":
            raise EmptyFileError(f"文件是空的：{self.path}")
        return text

    def split(self, text):
        if self.lang == "zh":
            raw = jieba.lcut(text)
        else:
            raw = text.lower().split()

        result = []
        for w in raw:
            w = w.strip(".,!?;:\"'()。，！？；：“”‘’（）")
            if w.strip() == "" or w in self.stop_words:
                continue
            result.append(w)
        return result

    def count_words(self):
        c = {}
        for w in self.words:
            c[w] = c.get(w, 0) + 1
        self.count = c
        return c

    def top(self, n=5):
        pairs = [(c, w) for w, c in self.count.items()]
        pairs.sort(reverse=True)
        return [(w, c) for c, w in pairs[:n]]

    def report(self, n=5):
        total = len(self.words)
        print("=" * 36)
        print(f"文件：{self.path}（{self.lang}）")
        print(f"总词数：{total}    不同词数：{len(self.count)}")
        print("=" * 36)
        for i, (w, c) in enumerate(self.top(n), start=1):
            if self.show_pct:
                pct = c / total if total else 0
                print(f"{i:>2}. {w:<10} {c:>3}  {pct:>6.1%}")
            else:
                print(f"{i:>2}. {w:<10} {c:>3}")

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


if __name__ == "__main__":
    try:
        cfg = load_config()
    except ConfigError as e:
        print(f"[失败] {e}")
        raise SystemExit(1)

    stops = load_stop_words(cfg["stop_words_file"])
    print(f"配置：语言={cfg['default_lang']}，显示前 {cfg['top_n']} 名，停用词 {len(stops)} 个")

    WordCounter(
        "../data/sample_zh.txt",
        lang=cfg["default_lang"],
        stop_words=stops,
        show_pct=cfg["show_pct"],
    ).run(cfg["top_n"])