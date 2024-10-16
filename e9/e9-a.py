import numpy as np


def numpy_demo():
    # 1. Create an array of all ones using np.ones()
    ones_array = np.ones((3, 4))  # A 3x4 array filled with ones
    print("Array of ones (3x4):")
    print(ones_array)

    # 2. Create an array of all zeros using np.zeros()
    zeros_array = np.zeros((2, 5))  # A 2x5 array filled with zeros
    print("\nArray of zeros (2x5):")
    print(zeros_array)

    # 3. Create an array of evenly spaced values using np.arange()
    range_array = np.arange(0, 10, 2)  # Array of numbers from 0 to 10 with a step of 2
    print("\nArray of values from 0 to 10 with step 2 (arange):")
    print(range_array)

    # 4. Reshape an array using np.reshape()
    reshaped_array = np.arange(1, 13).reshape(
        (3, 4)
    )  # Reshaping a 1D array into a 3x4 2D array
    print("\nReshaped array (from 1D to 3x4):")
    print(reshaped_array)

    # 5. Create an identity matrix using np.eye()
    identity_matrix = np.eye(4)  # A 4x4 identity matrix
    print("\nIdentity matrix (4x4):")
    print(identity_matrix)

    # 6. Create a random array using np.random.rand()
    random_array = np.random.rand(3, 3)  # A 3x3 array of random values between 0 and 1
    print("\nRandom array (3x3):")
    print(random_array)

    # 7. Flatten a multi-dimensional array using np.flatten()
    flattened_array = reshaped_array.flatten()  # Flatten the 3x4 array into a 1D array
    print("\nFlattened array:")
    print(flattened_array)

    # 8. Basic mathematical operations on arrays
    array1 = np.array([1, 2, 3])
    array2 = np.array([4, 5, 6])
    added_array = array1 + array2  # Element-wise addition
    multiplied_array = array1 * array2  # Element-wise multiplication
    print("\nElement-wise addition of arrays:")
    print(added_array)
    print("Element-wise multiplication of arrays:")
    print(multiplied_array)


# Call the function to demonstrate the usage of NumPy functions
numpy_demo()
