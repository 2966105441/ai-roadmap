f = open("../data/sample_en.txt",encoding = "utf-8")
text = f.read()
f.close()

print(f"读到{len(text)}个字符")
print(text[:60])


with open("../data/sample_en.txt",encoding="utf-8") as f:
    text = f.read()

print(f"读到{len(text)}个字符")