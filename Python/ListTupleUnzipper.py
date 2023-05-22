def unzip_list_of_tuples(lst):
    unzipped = list(zip(*lst))
    return unzipped

# Example usage
list_of_tuples = [(1, 'a'), (2, 'b'), (3, 'c')]

unzipped_lists = unzip_list_of_tuples(list_of_tuples)

# Print the unzipped lists
for lst in unzipped_lists:
    print(lst)
