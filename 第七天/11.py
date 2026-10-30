# ========== 每个函数只干一件事 ==========
STOP_WORDS = {
    "the", "a", "an", "is", "are", "and", "or", "to", "of", "in", "on",
    "it", "this", "that", "how", "we", "your", "but", "then",
    "do", "does", "can", "not", "be", "with", "why", "most",
    "often", "first", "right", "good", "alone", "what", "them",
}

def load_text(path):
    """读文件，返回全部文本。读失败就返回空字符串"""
    try:
        with open(path, encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print(f"找不到文件：{path}")
        return ""


def clean_words(text, stop_words=None):
    """切词 + 转小写 + 去标点 + 去停用词，返回干净的词列表"""
    if stop_words is None:              # 记住昨天的坑：默认值写 None
        stop_words = set()
    words = []
    for w in text.lower().split():
        w = w.strip(".,!?;:\"'()")      # 去掉两头的标点
        if w == "":
            continue
        if w in stop_words:
            continue
        words.append(w)
    return words


def count_words(words):
    """统计词频，返回 {词: 次数}"""
    count = {}
    for w in words:
        count[w] = count.get(w, 0) + 1
    return count


def top_n(count, n=10):
    """取前 n 名，返回 [(词, 次数), ...]"""
    pairs = []
    for w, c in count.items():
        pairs.append((c, w))           # 次数放前面，排序就按次数
    pairs.sort(reverse=True)
    result = []
    for c, w in pairs[:n]:
        result.append((w, c))           # 换回来，好读
    return result


def show_report(word_count, total, top):
    """打印报告"""
    print("=" * 34)
    print(f"总词数：{total}")
    print(f"不同词数：{word_count}")
    print("=" * 34)
    print("Top 10：")
    for i, (w, c) in enumerate(top, start=1):
        bar = "█" * c                   # 用方块做柱状图
        print(f"{i:>2}. {w:<14} {c:>3}  {bar}")


def main(path, n=10):
    text = load_text(path)
    if text == "":
        return
    words = clean_words(text,STOP_WORDS)
    count = count_words(words)
    top = top_n(count, n)
    show_report(len(count), len(words), top)


main("../data/sample_en.txt",n=5)
main("../data/sample_zh.txt")