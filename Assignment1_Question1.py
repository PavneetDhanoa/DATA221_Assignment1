# Controlled Multiplication Loop -- Question 1

# Threshold value
threshold = 100
product = 1

# keep track of the current multiplier
current_number = 1

# Multiply consecutive integers until the product exceeds the threshold
while product <= threshold:
    product = product * current_number
    current_number = current_number + 1

# Printing the final product
print("Final product:", product)

# Printing the integer that caused the product to exceed the threshold
print("Integer that caused the product to exceed the threshold:", current_number - 1)
