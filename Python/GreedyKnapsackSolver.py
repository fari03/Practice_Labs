def knapsack_greedy(values, weights, capacity):
    n = len(values)
    ratios = [(values[i] / weights[i], values[i], weights[i]) for i in range(n)]
    ratios.sort(reverse=True)

    max_value = 0
    selected_items = []

    for ratio, value, weight in ratios:
        if capacity >= weight:
            max_value += value
            selected_items.append((value, weight))
            capacity -= weight

    return max_value, selected_items

# Example usage
values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50

max_value, selected_items = knapsack_greedy(values, weights, capacity)

print("Maximum Value:", max_value)
print("Selected Items:")
for item in selected_items:
    print("Value:", item[0], "Weight:", item[1])
