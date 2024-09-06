# Creating a set
my_set = {1, 2, 3, 4, 5}
print("Initial set:", my_set)

# Adding an element to the set
my_set.add(6)
print("\nAfter adding 6:", my_set)

# Removing an element from the set (raises KeyError if the element doesn't exist)
my_set.remove(2)
print("\nAfter removing 2:", my_set)

# Discarding an element from the set (doesn't raise an error if the element is not present)
my_set.discard(7)  # No error, even though 7 is not in the set
print("\nAfter discarding 7 (non-existent element):", my_set)

# Using pop (removes and returns an arbitrary element)
removed_element = my_set.pop()
print("\nAfter popping an element:", my_set)
print("Popped element:", removed_element)

# Checking if an element exists in the set
print("\nIs 3 in the set?", 3 in my_set)

# Finding the union of two sets
another_set = {4, 5, 6, 7, 8}
union_set = my_set.union(another_set)
print("\nUnion of sets:", union_set)

# Finding the intersection of two sets
intersection_set = my_set.intersection(another_set)
print("\nIntersection of sets:", intersection_set)

# Finding the difference of two sets (elements in my_set but not in another_set)
difference_set = my_set.difference(another_set)
print("\nDifference of sets (my_set - another_set):", difference_set)

# Finding the symmetric difference (elements in either set, but not in both)
sym_diff_set = my_set.symmetric_difference(another_set)
print("\nSymmetric difference of sets:", sym_diff_set)

# Clearing all elements from the set
my_set.clear()
print("\nAfter clearing the set:", my_set)
