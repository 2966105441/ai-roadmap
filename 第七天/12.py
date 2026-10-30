def count_lines(path):
    """返回文件行数"""
    n = 0
    with open(path,"r",encoding="utf-8") as f:
        for line in f:
            n += 1
    return n


def append_line(path,text):
    """在文件末尾追加一行"""
    with open(path,"a",encoding = "utf-8") as f:
        f.write(text+"\n")



def find_word(text,word):
    """统计某个词出现的次数，不区分大小写"""
    target = word.lower()
    n = 0
    for w in text.lower().split():
        w = w.strip(".,!?")
        if w == target:
            n += 1
    return n

def longest_line(path):
    """返回最长的行（已去掉首尾空白）"""
    best = ""
    with open(path,"r",encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if len(line) > len(best):
                best = line
    return best

def export_top(top,path):
    """把[(词，次数),...]写成CSV风格的文件"""
    with open(path,"w",encoding = "utf-8") as f:
        for w,c in top:
            f.write(f"{w},{c}\n")


