import numpy as np

def slice_ndarray(arr, start, end):
    sliced_arr = arr[start:end]
    return sliced_arr

# Example usage
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

start_index = 2
end_index = 7

sliced_array = slice_ndarray(arr, start_index, end_index)
print(sliced_array)
