num1 = 0
num2 = 1

def func1 (a, b) :
    return a + b
def func2 (a, b):
    return a - b
def func3 (a, b):
    return func1 (a, 5) + func2 (5, b)

result = func3 (num1, num2)
print (result)