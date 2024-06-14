
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
#             # total_sum = Filtering.calculate_total(cart.cart)  # Use Filtering class method
#             # print(f"Total: ${total_sum:.2f}")







class CheckOut:
    @staticmethod
    def view_cart(cart):  # No need for staticmethod
        if not cart.cart:  # Access the 'cart' attribute of the Cart object
            print("Your cart is empty.")
        else:
            print("\nItems in Cart:")
            for item in cart.cart:  # Access the 'cart' attribute of the Cart object
                if 'name' in item:
                    print(item['name'], item['no'], item['price'])
                else:
                    print("Item missing name:", item['no'])
            # total_sum = Filtering.calculate_total(cart.cart)  # Use Filtering class method
            # print(f"Total: ${total_sum:.2f}")
