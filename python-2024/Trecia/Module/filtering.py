# from checkout import CheckOut  # Import CheckOut class here


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
    
    @staticmethod
    def calculate_total(cart):
        total_sum = 0
        for item in cart:
            total_sum += float(item['price'])  
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
            total_sum = cart.calculate_total(cart)  # Use CheckOut class method
            print(f"Total: ${total_sum:.2f}")
