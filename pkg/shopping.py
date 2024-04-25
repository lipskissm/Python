from cart import Cart
from file_reading import FileReading
from filtering import Filtering

class Controller:
    def __init__(self):
        self.cart = Cart()  # Initialize the Cart instance here

    def start_shopping(self):
        file_reader = FileReading()  # Create an instance of FileReading
        categories = file_reader.read_file_and_get_categories()  # Use the instance

        self.cart.load_cart_from_file('checkout_info.csv')  # Use the cart instance

        print(f"Available categories: {categories}")
        filter_instance = Filtering(file_reader.data)
        filter_by = input("Enter category to filter by: ")
        filtered_items = filter_instance.filter_items_by_category(filter_by)

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
                self.cart.add_to_cart(file_reader.data)
            elif choice == '2':
                self.cart.remove_from_cart()
                FileReading.save_to_csv('checkout_info.csv', self.cart.cart)
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

        FileReading.save_to_csv('checkout_info.csv', self.cart.cart)
        return self.cart
