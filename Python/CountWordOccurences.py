def count_word_occurrences(file_path, word):
    count = 0

    with open(file_path, 'r') as file:
        for line in file:
            words = line.strip().split()
            for w in words:
                if w.lower() == word.lower():
                    count += 1

    return count


# Example usage
file_path = 'text_file.txt'
word_to_count = 'example'

occurrences = count_word_occurrences(file_path, word_to_count)
print(f"The word '{word_to_count}' occurs {occurrences} times in the file.")
