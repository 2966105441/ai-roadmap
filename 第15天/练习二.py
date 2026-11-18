import functools

def 只跑一次(func):
    done = {"ok": False}
    cache = None

    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        nonlocal cache
        if done["ok"]:
            print("  （用上次的结果）")
            return cache
        cache = func(*args,**kwargs)
        done["ok"] = True
        return cache
    return wrapper

@只跑一次
def 慢活():
    print("  真正执行了一次")
    return 42

print(慢活())
print(慢活())
print(慢活())




def update(self, name: str, new_phone: str | None = None) -> None:
    name = name.strip()
    if name not in self.contacts:
        raise ContactError(f"通讯录里没有 {name}")
    if new_phone is None:
        return                      # 没传电话，什么都不改
    new_phone = new_phone.strip()
    if not new_phone.isdigit() or len(new_phone) != 11:
        raise ContactError(f"电话必须是 11 位数字，你给的是 {new_phone!r}")
    self.contacts[name] = new_phone
    self.save()