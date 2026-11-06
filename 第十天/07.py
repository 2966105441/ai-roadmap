import jieba

s = "我爱自然语言处理"
g = jieba.cut(s)
print("cut返回的是：",type(g))
print("转成列表看：",list(g))
print("lcut直接给：",jieba.lcut(s))