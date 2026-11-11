import json
result = {"检索":6,"质量":6,"模型":4}

#写进去
with open("result.json","w",encoding="utf-8") as f:
    json.dump(result,f,ensure_ascii=False,indent=2)

print("--- 文件内容 ---")
print(open("result.json",encoding="utf-8").read())


#读回来
with open("result.json",encoding="utf-8") as f:
    back = json.load(f)

print("--- 读回来 ---")
print(back)
print(type(back))