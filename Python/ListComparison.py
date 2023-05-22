def find_missing_and_additional_values(list1, list2):
    missing_values = []
    additional_values = []

    # Find missing values in list2
    for item in list1:
        if item not in list2:
            missing_values.append(item)

    # Find additional values in list2
    for item in list2:
        if item not in list1:
            additional_values.append(item)

    return missing_values, additional_values


# Example usage
list1 = [1, 2, 3, 4, 5]
list2 = [2, 3, 6, 7]

missing, additional = find_missing_and_additional_values(list1, list2)

print("Missing values:", missing)
print("Additional values:", additional)
