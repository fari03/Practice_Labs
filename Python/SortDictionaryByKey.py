from collections import OrderedDict

def sort_dictionary_by_key(dictionary):
    sorted_dict = OrderedDict(sorted(dictionary.items()))
    return sorted_dict

# Example usage
my_dict = {'c': 3, 'a': 1, 'b': 2}
sorted_dict = sort_dictionary_by_key(my_dict)

print("Sorted Dictionary by Key:")
for key, value in sorted_dict.items():
    print(key, value)
