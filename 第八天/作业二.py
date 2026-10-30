#测试一
class Book:
    def __init__(self,title,author,price):
        self.title = title
        self.author = author
        self.price = price
    def __str__(self):
        return f"《{self.title}》￥{self.price:.2f}"

b1 = Book("Python编程","张三",89.5)
b2 = Book("深度学习","李四",129.0)
print(b1.title,b1.author)
print(b2.title,b2.price)
print(b1)