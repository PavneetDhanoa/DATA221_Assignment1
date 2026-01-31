"""
    Computes base_value raised to the power of exponent_value.

"""
def power(base_value, exponent_value):
    return base_value ** exponent_value

# List of pairs (base, exponent)
pairs = [[5, 2], [3, -1], [4, 3], [2, 0]]

# List to store results
results = []

# Loop through each pair
for base_value, exponent_value in pairs:

    # Skip pairs with negative exponent
    if exponent_value < 0:
        continue

    # resulted powered output
    computed_result = power(base_value, exponent_value)

    # Store the result in the list
    results.append(computed_result)

# printing the final result list
print(results)
