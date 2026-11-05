class Demo:
    def __enter__(self):
        print("  [__ender__] 进入")
        return self
    def __exit__(self,exc_type,exc_val,tb):
        print("  [__exit__]不管怎样都会执行")
        return False

with Demo() as d:
    print("  [with 体] 干活")  