import itertools
vowels = ['a', 'e', 'i', 'o', 'u']
all_strings = []

for length in range(1, 6):
    for combination in itertools.product(vowels, repeat=length):
        all_strings.append(''.join(combination))

print(all_strings)
