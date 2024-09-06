# Initial dictionary
my_dict = {"name": "Alice", "age": 25, "city": "New York"}

# Traverse the dictionary (iterate over key-value pairs)
print("Traversing the dictionary:")
for key, value in my_dict.items():
    print(f"{key}: {value}")

# Add a new item to the dictionary
print("\nAdding a new item (country: USA):")
my_dict["country"] = "USA"
print(my_dict)

# Delete an item from the dictionary (e.g., remove 'age')
print("\nDeleting the item with key 'age':")
my_dict.pop("age")
print(my_dict)

# Replace an existing item (e.g., update 'city' to 'Los Angeles')
print("\nReplacing the value of 'city' with 'Los Angeles':")
my_dict["city"] = "Los Angeles"
print(my_dict)

# Optional: Traversing after modifications
print("\nFinal state of the dictionary after modifications:")
for key, value in my_dict.items():
    print(f"{key}: {value}")
