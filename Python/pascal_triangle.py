def print_pascals_triangle(n):
    if n < 1:
        return

    # Initialize the first row of the triangle with a 1
    row = [1]
    print(row)

    for i in range(1, n):
        # Compute the next row of the triangle
        next_row = [1] * (i + 1)
        for j in range(1, i):
            next_row[j] = row[j - 1] + row[j]
        print(next_row)
        row = next_row
print_pascals_triangle(5)
