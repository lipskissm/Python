import csv

class FileReading:
    data = []
    categories = set()

    @staticmethod
    def read_file_and_get_categories():
        filename = input("Enter file name: ")
        with open(filename, 'r', newline='') as file:
            read = csv.DictReader(file)
            for row in read:
                FileReading.data.append(row)
                FileReading.categories.add(row['category'])
        return FileReading.categories
    
    @staticmethod
    def save_to_csv(filename, data):
        fieldnames = data[0].keys() if data else []
        with open(filename, 'w', newline='') as file:  # Change 'a' to 'w' for write mode
            writer = csv.DictWriter(file, fieldnames=fieldnames)
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

class Controller:
    @staticmethod
    def start_shopping():
        # Load data from CSV
        categories = FileReading.read_file_and_get_categories()
        
        # Load cart from checkout_info.csv
        Cart.load_cart_from_file('checkout_info.csv')

        print(f"Available categories: {categories}")
        filter_instance = Filtering(FileReading.data)
        filter_by = input("Enter category to filter by: ")
        filtered_items = filter_instance.filter_items_by_category(filter_by)

        # Print filtered items
        for item in filtered_items:
            if 'name' in item:
                print(item['name'], item['no'])
            else:
                print("Item missing name:", item)

        while True:
            choice = input("Select an action: 1 - Add to cart, 2 - Remove from cart, 3 - Filter and shop again, exit - Finish shopping: ")
            if choice.lower() == 'exit':
                break
            elif choice == '1': 
                Cart.add_to_cart()
            elif choice == '2':
                Cart.remove_from_cart()
                # Save updated cart to CSV after removing item
                FileReading.save_to_csv('checkout_info.csv', Cart.cart)
            elif choice == '3':
                filter_by = input("Enter category to filter by: ")
                filtered_items = filter_instance.filter_items_by_category(filter_by)
                for item in filtered_items:
                    if 'name' in item:
                        print(item['name'], item['no'])
                    else:
                        print("Item missing name:", item)
            else:
                print("Invalid choice.")

        print("\nItems in Cart:")
        for item in Cart.cart:
            if 'name' in item:
                print(item['name'], item['no'])
            else:
                print("Item missing name:", item)

        FileReading.save_to_csv('checkout_info.csv', Cart.cart)

class Cart:
    cart = []

    @staticmethod
    def load_cart_from_file(filename):
        Cart.cart = FileReading.load_from_csv(filename)

    @staticmethod
    def add_to_cart():
        while True:
            no = input("Enter item ID to add to cart (type 'exit' to quit): ")
            if no.lower() == 'exit':
                break
            
            found_item = False
            for item in FileReading.data:
                if item['no'] == no:
                    add_confirm = input(f"Add {item.get('name', 'Unknown')} to cart? (Yes/No): ")
                    if add_confirm.lower() == 'yes':
                        Cart.cart.append(item)
                        print(f"Added {item.get('name', 'Unknown')} to cart.")
                    else:
                        print(f"{item.get('name', 'Unknown')} not added to cart.")
                    found_item = True
                    break

            if not found_item:
                print("Item not found.")

    @staticmethod
    def remove_from_cart():
        while True:
            print("Current items in your cart:")
            for item in Cart.cart:
                if 'name' in item:
                    print(item['name'], item['no'])
                else:
                    print("Item missing name:", item['no'])
            
            no = input("Enter item ID to remove from cart (type 'exit' to quit): ")
            if no.lower() == 'exit':
                break

            item_found = False
            for item in Cart.cart:
                if item['no'] == no:
                    remove_conf = input(f"Remove {item.get('name', 'Unknown')} from cart? (Yes/no): ")
                    if remove_conf.lower() == 'yes':
                        Cart.cart.remove(item)
                        print("Item removed")
                    else:
                        print("Removing canceled")
                    item_found = True
                    break

            if not item_found:
                print("Item not found in cart.")

class Filtering:
    def __init__(self, data):
        self.data = data
        self.filtered_items = []

    def filter_items_by_category(self, category):
        self.filtered_items.clear()  # Clear previous filtered items
        for item in self.data:
            if item['category'].lower() == category.lower():
                self.filtered_items.append(item)
        return self.filtered_items

class CheckOut:
    @staticmethod
    def calculate_total(cart):
        total_sum = 0
        for item in cart:
            total_sum += float(item['price'])  # Assuming 'price' is a key in the item dictionary
        return total_sum

    @staticmethod
    def view_cart(cart):
        if not cart:
            print("Your cart is empty.")
        else:
            print("\nItems in Cart:")
            for item in cart:
                if 'name' in item:
                    print(item['name'], item['no'], item['price'])
                else:
                    print("Item missing name:", item['no'])
            total_sum = CheckOut.calculate_total(cart)
            print(f"Total: ${total_sum:.2f}")

# Example usage
if __name__ == "__main__":
    Controller.start_shopping()
    CheckOut.view_cart(Cart.cart)
