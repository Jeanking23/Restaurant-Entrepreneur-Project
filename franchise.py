from orderfactory import OrderFactory
from order import Order
from logger import Logger

class Franchise:

    def __init__(self, location_number):
        self.location_number = location_number
        self.logger = Logger()
        self.orderfactory = OrderFactory()

    def location_number(self, dish_name) :
        if dish_name == "pizza":
           return 1
        if dish_name == "pasta":
           return 2
        if dish_name == "salad":
           return 3

    def place_order(self, franchise_name, dish_name, price):
        self.orderfactory = OrderFactory()
        self.order = self.orderfactory.create_order(dish_name, price)

        self.order = self.orderfactory.create_order(dish_name, price)
        welcome_message = f"Welcome to TB Restaurant, location #{self.location_number}"
        print(welcome_message)
        self.logger.log_transaction( franchise_name, self.order.dish_name, price)
