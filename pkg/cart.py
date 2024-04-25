from file_reading import FileReading

class Cart:
    def __init__(self):
        self.cart = []
    
    def load_cart_from_file(self, filename):
        self.cart = FileReading.load_from_csv(filename)

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
                        self.cart.append(item)
                        print(f"Added {item.get('name', 'Unknown')} to cart.")
                        # Save cart to file after adding an item
                        FileReading.save_to_csv('checkout_info.csv', self.cart)
                    else:
                        print(f"{item.get('name', 'Unknown')} not added to cart.")
                    found_item = True
                    break

            if not found_item:
                print("Item not found.")

    def remove_from_cart(self):
        while True:
            print("Current items in your cart:")
            for item in self.cart:
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
                        # Save cart to file after removing an item
                        FileReading.save_to_csv('checkout_info.csv', self.cart)
                    else:
                        print("Removing canceled")
                    item_found = True
                    break

            if not item_found:
                print("Item not found in cart.")
