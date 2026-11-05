def read_or_default(path,defult=""):
    try:
        with open(path,encoding = "utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return defult
