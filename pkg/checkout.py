from file_reading import FileReading

class Cart:
    def __init__(self):
        self.cart = []
    
    def load_cart_from_file(self,filename):
        self.cart = FileReading.load_from_csv(filename)








# class CheckOut:
#     @staticmethod
#     def view_cart(cart):  # No need for staticmethod
#         if not cart.cart:  # Access the 'cart' attribute of the Cart object
#             print("Your cart is empty.")
#         else:
#             print("\nItems in Cart:")
#             for item in cart.cart:  # Access the 'cart' attribute of the Cart object
#                 if 'name' in item:
#                     print(item['name'], item['no'], item['price'])
#                 else:
#                     print("Item missing name:", item['no'])
#             total_sum = Filtering.calculate_total(cart.cart)  # Use Filtering class method
#             print(f"Total: ${total_sum:.2f}")
