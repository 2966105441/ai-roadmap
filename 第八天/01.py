msg = {"role":"user","content":"你好"}
msg["rol"] = "user"
print(msg)

# 不用类：
#   数据（path / words / count）  ←  散落各处的变量
#   函数（load / clean / count）  ←  各自独立，靠参数传递
#
# 用类：
#   ┌─────────── WordCounter ───────────┐
#   │  数据：path、words、count          │   ← 装在盒子里
#   │  函数：load()、clean()、count()    │   ← 也装在盒子里
#   └───────────────────────────────────┘
#   盒子外面只说一句：c = WordCounter(路径);  c.run()