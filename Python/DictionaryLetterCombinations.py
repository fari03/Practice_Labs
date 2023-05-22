from itertools import product

def generate_letter_combinations(dictionary):
    keys = dictionary.keys()
    values = [dictionary[key] for key in keys]
    combinations = product(*values)
    combinations_list = [''.join(combination) for combination in combinations]
    return combinations_list

# Example usage
my_dict = {
    'key1': ['a', 'b', 'c'],
    'key2': ['x', 'y'],
    'key3': ['p', 'q', 'r']
}

letter_combinations = generate_letter_combinations(my_dict)

print("Letter Combinations:")
for combination in letter_combinations:
    print(combination)
