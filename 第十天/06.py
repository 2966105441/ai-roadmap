import jieba

s = "人工智能正在改变我们构建软件的方式"

print("用split：",s.split())
print("用jieba：",jieba.lcut(s))
print("split切出几个词：",len(s.split()))
print("jieba切出几个词：",len(jieba.lcut(s))) 