# Python program to access tuple elements
my_tuple = ("I", "Love", "To", "Code", "In", "Python")
print("Tuple:", my_tuple)

print("Element at index 1:", my_tuple[1])
print("Element at index 5:", my_tuple[5])

# IndexError: list index out of range
# print(my_tuple[10])

# Index must be an integer
# TypeError: list indices must be integers, not float
# my_tuple[5.0]


# Python program to access tuple elements
my_tuple = ("I", "Love", "To", "Code", "In", "Python")
print("Tuple:", my_tuple)

print("Element at index -1:", my_tuple[-1])
print("Element at index -5:", my_tuple[-3])
