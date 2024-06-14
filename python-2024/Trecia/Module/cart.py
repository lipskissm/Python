from FileModule.file_reading import FileReading

class Cart:
    def __init__(self):
        self.cart = []
        self.loaded_from_file = False  # Track if cart has been loaded from file
    
    def load_cart_from_file(self, filename):
        self.cart = FileReading.load_from_csv(filename)
        self.loaded_from_file = True  # Set loaded_from_file to True after loading from file
    
    def add_to_cart(self, data):
        while True:
            no = input("Enter item ID to add to cart (type 'exit' to quit): ")
            if no.lower() == 'exit':
                break
            
            found_item = False
            for item in data:
                if item['no'] == no:
                    add_confirm = input(f"Add {item.get('name', 'Unknown')} to cart? (Yes/No): ")
                    if add_confirm.lower() == 'yes':
                        self.cart.append(item)  # Add item directly to the cart attribute
                        print(f"Added {item.get('name', 'Unknown')} to cart.")
                        found_item = True
                        break  # No need to continue searching once item is added to cart

            if not found_item:
                print("Item not found.")

    def remove_from_cart(self, loaded_data):
        cart_items = self.cart + loaded_data  # Merge loaded data with current cart items
        while True:
            print("Current items in your cart:")
            for item in cart_items:
                if 'name' in item:
                    print(item['name'], item['no'])
                else:
                    print("Item missing name:", item['no'])
            
            no = input("Enter item ID to remove from cart (type 'exit' to quit): ")
            if no.lower() == 'exit':
                break

            item_found = False
            for item in self.cart:
                if item['no'] == no:
                    remove_conf = input(f"Remove {item.get('name', 'Unknown')} from cart? (Yes/no): ")
                    if remove_conf.lower() == 'yes':
                        self.cart.remove(item)
                        print("Item removed")
                        FileReading.save_to_csv('checkout_info.csv', self.cart)  # Save cart to file after removing an item
                    else:
                        print("Removing canceled")
                    item_found = True
                    break

            if not item_found:
                print("Item not found in cart.")
