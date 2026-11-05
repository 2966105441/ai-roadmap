def safe_int(s,default=0):
    try:
        return int(s)
    except (ValueError, TypeError):
        return default

print(safe_int("12"),safe_int("abc"),safe_int(None),safe_int("abc",-1))