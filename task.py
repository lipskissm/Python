import csv
import sys

def read_csv(filename):
    data = []
    with open(filename, 'r', newline='') as file:
        read = csv.DictReader(file)
        for row in read:
            data.append(row)
    return data
    

def group_and_calculate(data, group_by, calculate):
    groups = {}
    for row in data:
        key = row[group_by]
        print (key)
        if key not in groups:
            groups[key] = []
        if row['price'] != '':
            groups[key].append(float(row['price']))
   
  

    calculated = {}
    for key, values in groups.items():
        if calculate == 'row_count':
            calculated[key] = len(values)
        elif calculate == 'row_count_percentage':
            calculated[key] = len(values) / len(data) * 100
        elif calculate == 'average_price':
            calculated[key] = sum(values) / len(values)
    return calculated

def print_results(results, limit=None):
    sorted_results = sorted(results.items(), key=lambda x: x[1], reverse=True)
    if limit is not None:
        sorted_results = sorted_results[:limit]
    for key, value in sorted_results:
        print(f'{key}: {value}')

if __name__ == "__main__":
    filename = sys.argv[1]
    group_by = sys.argv[2]
    calculate = sys.argv[3]
    limit = int(sys.argv[4]) if len(sys.argv) == 5 else None

    data = read_csv(filename)
    results = group_and_calculate(data, group_by, calculate)
    print_results(results, limit)
   
   
