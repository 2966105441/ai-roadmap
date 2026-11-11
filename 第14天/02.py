from book import ContactBook

book = ContactBook("../data/contacts.csv")

print(f"len(book) = {len(book)}")
print(f"'张三' in book = {'张三' in book}")
print(f"'王五五' in book = {'王五五' in book}")
print("-" * 30)
print(book)