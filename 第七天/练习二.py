def longest_line(path):
    """返回最长的行（已去掉首尾空白）"""
    best = ""
    with open(path,"r",encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if len(line) > len(best):
                best = line
    return best

print(longest_line("../data/sample_en.txt"))
