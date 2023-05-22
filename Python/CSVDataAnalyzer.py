import csv
from collections import defaultdict
import statistics

def read_csv_file(file_path):
    data = defaultdict(list)

    with open(file_path, 'r') as file:
        reader = csv.reader(file)

        headers = next(reader)

        for row in reader:
            for i, value in enumerate(row):
                if value.strip() == '':
                    row[i] = None
            for header, value in zip(headers, row):
                data[header].append(value)

    return data


def calculate_means(data):
    means = {}

    for header, values in data.items():
        numeric_values = [v for v in values if v is not None and isinstance(v, (int, float))]
        if numeric_values:
            means[header] = statistics.mean(numeric_values)
        else:
            means[header] = None

    return means


# Example usage
file_path = 'data.csv'
csv_data = read_csv_file(file_path)
means = calculate_means(csv_data)

for header, mean in means.items():
    print(f"Mean of '{header}': {mean}")
