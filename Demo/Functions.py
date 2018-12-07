"""
Python Functions
"""
def printHello():
    print("Hello")
printHello()

"""
function parameter
"""
def printHi(name="John"):
    print("hi, "+name)
printHi("Raghav")
printHi()

def sum(a,b,c):
    print(a+b+c)
sum(10,20,30)

def returnSum(a,b):

    return (a+b)
x = returnSum(10,20)
print(x)
