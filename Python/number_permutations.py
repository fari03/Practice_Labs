import itertools

numbers = [1, 2, 3]
all_permutations = []

for permutation in itertools.permutations(numbers):
    all_permutations.append(permutation)

print(all_permutations)
