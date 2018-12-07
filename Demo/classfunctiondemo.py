"""
Classes Functions Objects
"""
class MyClass:
    namestart = 'Raghav'
    def __init__(self, year, age):
        self.year = year
        self.age = age

    def show(self):
        print(self.year, "+", self.age, "= ", self.year + self.age)
    def sum(self,a, b):
        print(a+b)

x = MyClass(10, 90)
x.show()
print(x.age)
x.sum(20,10)

class FC:
    def __init__(self,one,ten):
        self.one = one
        self.ten = ten
    def show(self):
        print(self.ten, "-", self.one, "= ", self.ten - self.one)

a = FC(one=1, ten=10)
a.show()
