"""
    Builds a dictionary where each key is a string from the given list and
    each value is a dictionary containing the string length and its parity.

"""
def build_string_dictionary(list_of_strings):

    #main dictionary
    string_dictionary = {}

    for single_string in list_of_strings:
        length_of_string = len(single_string)

        if length_of_string % 2 == 0:
            parity = "even"
        else:
            parity = "odd"

        string_dictionary[single_string] = {
            "length": length_of_string,
            "parity": parity
        }

    return string_dictionary

#sample words
words = ["data", "science"]

result = build_string_dictionary(words)
print(result)
