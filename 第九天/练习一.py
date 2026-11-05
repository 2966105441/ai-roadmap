def get_number():
    for i in range(3):
        s = input("请输入一个数字：")
        try:
            return float(s)
        except ValueError:
            print(f"  [{s}]不是数字，还剩{2 - i}次机会")
    print("  三次都错了，放弃")
    return None

print("结果：",get_number())