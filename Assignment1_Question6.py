def distribution_analysis(numbers):
    """
    Builds a dictionary where each key is a unique value from the list
    and each value is the percentage of elements in the list that are
    less than or equal to that key.

    """

    # Total number of elements in the list
    total_count = len(numbers)

    # Dictionary to store the final results
    distribution_dictionary = {}

    # Get unique values and sort them
    unique_sorted_values = sorted(set(numbers))

    # For each unique value, calculate percentage of values <= that value
    for value in unique_sorted_values:
        count_less_or_equal = 0

        for number in numbers:
            if number <= value:
                count_less_or_equal += 1

        percentage = (count_less_or_equal / total_count) * 100
        distribution_dictionary[value] = percentage

    return distribution_dictionary

numbers = [3, 1, 2, 3, 4, 2]
print(distribution_analysis(numbers))

