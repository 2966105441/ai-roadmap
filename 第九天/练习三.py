def show(s):
    try:
        v = int(s)
    except ValueError:
        print("  不是数字")
    else:
        print(f"  是数字：{v}")

show("7")
show("x")