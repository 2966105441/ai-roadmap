import json
d = {"检索":6,"模型":4}

print("1)不加 ensure_ascii：")
print(json.dumps(d))

print("2)加了 ensure_ascii=False：")
print(json.dumps(d, ensure_ascii=False))

print("3) 再加 indent=2：")
print(json.dumps(d,ensure_ascii=False,indent=2))

print("4) 紧凑版 separators：")
print(json.dumps(d,ensure_ascii=False,separators=(",",":")))