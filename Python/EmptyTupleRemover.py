def remove_empty_tuples(lst):
    result = [t for t in lst if t]
    return result

# Example usage
tuples_list = [(1, 2), (), (3,), (4, 5, 6), (), (), (7,)]

filtered_list = remove_empty_tuples(tuples_list)

print("Filtered List of Tuples:")
print(filtered_list)
