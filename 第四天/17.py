sums = [1,2,3,4,5]
print(sums[::-1])

sums.reverse()
print(sums)


line = "人工智能 正在  改变 世界"
words = line.split()
print(words)
print(len(words))

print("/".join(words))


lenght = []
for word in words:
    if len(word) > 2:
        lenght.append(word)
print(lenght)