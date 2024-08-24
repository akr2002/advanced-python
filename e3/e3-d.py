from operator import eq

# Python program to create Tuples
# empty tuple
my_tuple = ()
print(my_tuple)

# tuple with integer values
num = (100, 35, 7, 21)
print(num)

# tuple with mixed values
my_tuple = (23.545, "Hello", "A", 785)
print(my_tuple)

# nested tuples
my_tuple = ("Python", [2, 4, 6], (1, 3, 5))
print(my_tuple)


# Python program to delete entire tuple
my_tuple = ("p", "r", "o", "g", "r", "a", "m", "m", "i", "n", "g")
print(my_tuple)

print("Count of letter g:", my_tuple.count("g"))
print("Index of letter a:", my_tuple.index("a"))


tup1 = ("A", "E", "G", "B")
tup2 = ("A", "Z", "E", "L")

if eq(tup1, tup2) != 0:
    print("Tuples are not same")
else:
    print("Tuples are same")

print("Max value in tup1 is:", max(tup1))
print("Min value in tup2 is:", min(tup2))
