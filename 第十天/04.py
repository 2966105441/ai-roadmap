from mypkg.text import clean,word_count

s = "  Hello World From Package  "
print(clean(s))
print(word_count(clean(s)))