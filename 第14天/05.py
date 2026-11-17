from book import ContactBook

a = ContactBook("../data/contacts.csv")
b = a
b.add("测试", "13000000000")

print(len(a))
print(len(b))
print(a is b)