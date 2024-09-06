# Function to count positive and negative numbers in a list
def count_pos_neg(numbers):
    count_dict = {"positive": 0, "negative": 0}

    # Traverse the list and update the dictionary based on the number's sign
    for num in numbers:
        if num > 0:
            count_dict["positive"] += 1
        elif num < 0:
            count_dict["negative"] += 1

    return count_dict


# Example list of numbers
numbers_list = [10, -3, 7, -5, 0, 8, -1, 4, -2]

# Call the function and store the result
result_dict = count_pos_neg(numbers_list)

# Print the result
print("Count of positive and negative numbers:", result_dict)
