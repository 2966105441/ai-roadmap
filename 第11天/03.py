def load_config(path="config.json"):
    """读配置文件；文件不在就用默认值"""
    if not os.path.exists(path):
        print(f"[提示] 没找到配置文件 {path}，用默认配置")
        return DEFAULT_CONFIG.copy()

    try:
        with open(path, encoding="utf-8") as f:
            cfg = json.load(f)
    except json.JSONDecodeError as e:
        raise ConfigError(
            f"config.json 第 {e.lineno} 行第 {e.colno} 列写错了：{e.msg}"
        ) from e

    for k, v in DEFAULT_CONFIG.items():
        cfg.setdefault(k, v)
    return cfg


def load_stop_words(path):
    """一行一个词；空行和 # 注释跳过"""
    if not path:
        return set()
    if not os.path.exists(path):
        print(f"[提示] 停用词表不存在：{path}，本次不过滤")
        return set()

    words = set()
    with open(path, encoding="utf-8") as f:
        for line in f:
            w = line.strip()
            if w == "" or w.startswith("#"):
                continue
            words.add(w)
    return words