#顺序：具体的写前面，笼统的写后面
try:
    open("nope.txt",encoding="utf-8")

except FileNotFoundError:
    print("这行永远走不到")
except OSError:
    print("被OSError抓住了（具体是哪个？不知道）")