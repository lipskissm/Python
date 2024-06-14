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
        return self.data
    
    @staticmethod
    def save_to_csv(filename, data):
        existing_data = FileReading.load_from_csv(filename)  # Load existing data from the file
        combined_data = existing_data + data  # Merge existing data with new data

        fieldnames = combined_data[0].keys() if combined_data else []
        with open(filename, 'w', newline='') as file:  # Open file in write mode ('w')
            writer = csv.DictWriter(file, fieldnames)
            writer.writeheader()
            writer.writerows(combined_data)


    @staticmethod
    def load_from_csv(filename):
        data = []
        with open(filename, 'r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append(row)
        return data

    @staticmethod
    def save_scraped_data(filename, scraped_data, category="new"):
        # Assign unique IDs starting from 3640
        current_id = 3694
        for item in scraped_data:
            item['no'] = current_id
            item['category'] = category
            current_id += 1
        
        # Write scraped_data to the CSV file
        with open(filename, 'w', newline='', encoding="utf-8") as file:
            fieldnames = list(scraped_data[0].keys()) if scraped_data else []
            writer = csv.DictWriter(file, fieldnames)
            writer.writeheader()
            writer.writerows(scraped_data)