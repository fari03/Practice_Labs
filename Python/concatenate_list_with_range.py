def concatenate_list(lst, n):
    return lst + list(range(1, n+1))

# example usage
lst = [1, 2, 3]
n = 5
concatenated_list = concatenate_list(lst, n)
print(concatenated_list)
