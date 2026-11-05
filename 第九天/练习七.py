# def load(p):
#   try:
#     return open(p, encoding="utf-8").read()
#   except:
#     return ""

#问题有三处：
#1.裸except：编码错误，权限错误，甚至你打错变量名，全部变成返回“”
#2.没有with：文件靠垃圾回收关，不保证及时
#3.失败和“文件真的是空的”返回了同一个值，调用方分不清

#改法：
def load(p):
    try:
        with open(p,encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print(f"[警告] 文件不存在：{p}")
        return None      #用None区分"失败"和"空文件"
    
