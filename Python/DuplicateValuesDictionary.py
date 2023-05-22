def create_dictionary(list1, list2):
    dictionary = {}

    # Iterate over the lists simultaneously
    for key, value in zip(list1, list2):
        if key in dictionary:
            # If the key already exists in the dictionary, append the value to the existing list
            dictionary[key].append(value)
        else:
            # If the key is not yet present, create a new key-value pair with a list containing the value
            dictionary[key] = [value]

    return dictionary

# Example usage
keys = ['a', 'b', 'c', 'a', 'b']
values = [1, 2, 3, 4, 5]

result_dict = create_dictionary(keys, values)

# Print the dictionary
for key, value in result_dict.items():
    print(key, value)
