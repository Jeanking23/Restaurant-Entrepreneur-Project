from order import Order
class Pizza(Order) :


    def __init__(self, dish_name, price):
        self.dish_name = dish_name
        self.price = price
