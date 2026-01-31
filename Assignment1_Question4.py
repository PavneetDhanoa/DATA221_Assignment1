from random import random

# 20 random values between 0 and 1
values = [random() for i in range(20)]

# a random threshold value x
x = random()


def find_indices_greater_or_equal(sorted_values, threshold_value):
    """
    Finds all indices in a sorted list where the value is
    greater than or equal to a given threshold.

    """
    matching_indices = []

    for index in range(len(sorted_values)):
        if sorted_values[index] >= threshold_value:
            matching_indices.append(index)

    return matching_indices


# Sort the list of values
values.sort()

# Find all indices where the value is greater than or equal to x
indices_greater_or_equal = find_indices_greater_or_equal(values, x)

# Printing the sorted list
print("Sorted list:", values)

# Printing the value of x
print("Value of x:", x)

# Printing the first matching index if it exists
if len(indices_greater_or_equal) > 0:
    print("First matching index:", indices_greater_or_equal[0])
else:
    print("No values greater than or equal to x were found.")
