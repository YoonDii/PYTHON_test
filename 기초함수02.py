a = 20
b = 30

def rectangle (a, b):
    return a * b , (a + b) * 2

print(rectangle(a, b))


## 멘토님 풀이

def rectangle (a, b):
    area = a * b
    perimeter = 2 * (a+b)
    return area , perimeter
print(rectangle (20, 30))