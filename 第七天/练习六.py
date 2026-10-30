def show_report(word_count,total,top):
    print("="*42)
    print(f"总词数：{total}  不同词数：{word_count}")
    print("="*42)
    print("排名  词          次数   占比")
    for i,(w,c)in enumerate(top,start=1):
        pct = c/total
        bar = "▮" * c
        print(f"{i:>2}.  {w:<14} {c:>3}  {pct:>5.1%}  {bar}")

main("../data/sample_en.txt")