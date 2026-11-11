import json
print(json.dumps({"a": True, "b": None}, ensure_ascii=False))
print(json.dumps([1, 2, 3]))
print(json.dumps({1: "x"}))