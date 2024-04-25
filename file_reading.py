import csv

class FileReading:
    def __init__(self):
        self.data = []
        self.categories = set()

    def read_file_and_get_categories(self):
        filename = input("Enter file name: ")
        with open(filename, 'r', newline='') as file:
            read = csv.DictReader(file)
            for row in read:
                self.data.append(row)
                self.categories.add(row['category'])
        return self.categories
    
    @staticmethod
    def save_to_csv(filename, data):
        fieldnames = data[0].keys() if data else []
        with open(filename, 'w', newline='') as file:  
            writer = csv.DictWriter(file, fieldnames)
            writer.writeheader()
            writer.writerows(data)

    @staticmethod
    def load_from_csv(filename):
        data = []
        with open(filename, 'r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append(row)
        return data
