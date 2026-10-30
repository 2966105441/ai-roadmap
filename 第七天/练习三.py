def export_top(top,path):
    """把[(词，次数),...]写成CSV风格的文件"""
    with open(path,"w",encoding = "utf-8") as f:
        for w,c in top:
            f.write(f"{w},{c}\n")
