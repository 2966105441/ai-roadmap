#返回数字
def add(a,b):
    return a + b

#返回字符串
def level(score):
    if score >= 90:
        return "优秀"
    return "还行"

#返回列表（批量挑出符合条件的）
def long_words(words,min_len=3):
    result = []
    for w in words:
        if len(w) >= min_len:
            result.append(w)
    return result

#返回字典（这就是API消息的格式）
def make_message(role,content):
    return {"role":role,"content":content}

print(add(3,5))
print(level(95))
print(long_words(["AI","是","未来","人工智能"]))
print(make_message("user","你好"))

