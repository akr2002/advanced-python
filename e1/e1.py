print("Arithmetic operators")
print("====================")
a = 7
b = 2
print("Sum: ", a + b)
print("Subtraction: ", a - b)
print("Multiplication: ", a * b)
print("Division: ", a / b)
print("Floor Division: ", a // b)
print("Modulo: ", a % b)
print("Power: ", a**b)
print("Assignment operators")
print("====================")
a = 10
b = 5
a += b  # a = a + b

print(a)
print("Comparison operators")
print("====================")
a = 5
b = 2
print("a == b =", a == b)
print("a != b =", a != b)
print("a > b =", a > b)
print("a < b =", a < b)
print("a >= b =", a >= b)
print("a <= b =", a <= b)
print("Logical operators")
print("=================")
print(True and True)  # True
print(True and False)  # False
print(True or False)  # True
print(not True)  # False
print("Bitwise operators")
print("=================")
x = 10
y = 4
print(x & y)
print(x | y)
print(-x)
print(x ^ y)
print(x >> 2)
print(x << 2)
print("Identity operators")
print("==================")
x1 = 5
y1 = 5
x2 = "Hello"
y2 = "Hello"
x3 = [1, 2, 3]
y3 = [1, 2, 3]
print(x1 is not y1)  # prints False
print(x2 is y2)  # prints True
print(x3 is y3)  # prints False
print("Membership operators")
print("====================")
message = "Hello world"
dict1 = {1: "a", 2: "b"}
print("H" in message)  # prints True
print("hello" not in message)  # prints True
print(1 in dict1)  # prints True
print("a" in dict1)  # prints False
