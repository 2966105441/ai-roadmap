import json
with open("profile.json",encoding="utf-8") as f:
    p = json.load(f)

print(f"{p['name']}，{p['age']} 岁，在{p['city']}")
print(f"会不会 Python：{p['knows_python']}（类型：{type(p['knows_python']).__name__}）")
print(f"爱好：{'、'.join(p['hobbies'])}")
print(f"想去：{p['target_company']}")