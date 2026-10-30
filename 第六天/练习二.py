def make_message(role,content):
    return {"role":role,"content":content}
print(make_message("user","xaxsxcas"))


def format_price(amount,symbol="￥"):
    return f"{symbol}{amount:.2f}"
print(format_price(19.9))
print(format_price(2.132,"$"))


def split_text(text,size=10):
    chunks = []
    for i in range(0,len(text),size):
        chunks.append(text[i:i+size])
    return chunks
text = "自然语言处理是人工智能的一个重要分支它研究如何让计算机理解人类语言"
result = split_text(text,10)
print(f"切成{len(result)}块")
for i,c in enumerate(result,start = 1):
    print(f" 第{i}块({len(c)}字):{c}")



