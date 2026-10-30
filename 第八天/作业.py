#测试一
class Book:
    def __init__(self,title,author,price):
        self.title = title
        self.author = author
        self.price = price

b1 = Book("Python编程","张三",89.5)
b2 = Book("深度学习","李四",129.0)
print(b1.title,b1.author)
print(b2.title,b2.price)

#作业二
class Book:
    def __init__(self,title,price):
        self.title = title
        self.price = price

    def discount(self,rate):
        self.price = self.price * rate
        return self.price

b = Book("Python编程",100)
print(b.discount(0.8))
print(b.price)


