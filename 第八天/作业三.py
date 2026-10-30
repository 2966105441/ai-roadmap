class Calculator:
    def __init__(self):
        self.value = 0
    def add(self,x):
        self.value = self.value + x
        return self
    def sub(self,x):
        self.value = self.value - x
        return self
    def result(self):
        return self.value

c = Calculator()
c.add(10).add(5).sub(3)
print(c.result())
