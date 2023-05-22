def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    less_than_pivot = [x for x in arr if x < pivot]
    equal_to_pivot = [x for x in arr if x == pivot]
    greater_than_pivot = [x for x in arr if x > pivot]

    return quick_sort(less_than_pivot) + equal_to_pivot + quick_sort(greater_than_pivot)


# Example usage
arr = [8, 3, 1, 5, 2, 9, 6, 4, 7]
sorted_arr = quick_sort(arr)
print("Sorted array using Quick Sort:", sorted_arr)
