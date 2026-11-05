def parse(s):
    try:
        v = int(s)
    except ValueError:
        print(f"[{s}]解析失败")
    else:
        print(f"[{s}]解析成功->{v}")

parse("123")
parse("abc")

#不管出什么事，我一定会执行：finally
def test_finally(x):
    try:
        print("  try 开始")
        return 10/x
    except ZeroDivisionError:
        print("  except：不能除以0")
        return None
    finally:
        print("  finally:我一定会执行")

print("x=2 ->",test_finally(2))
print("x=0 ->",test_finally(0))