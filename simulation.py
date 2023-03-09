from franchise import Franchise
from logger import Logger
from orderfactory import OrderFactory


class Simulation:
    def __init__(self):
        self.franchise = Franchise(1)  # create Franchise instance with location number 1
        self.logger = Logger()
        self.orderfactory = OrderFactory()

    def run_simulation(self):
        store_one = Franchise(1)
        store_two = Franchise(2)
        store_three = Franchise(3)

        store_one.place_order("pizza", 10)
        store_two.place_order("pasta", 8)
        store_one.place_order("salad", 6)
        store_two.place_order("pizza", 10)
        store_three.place_order("pasta", 8)
        store_three.place_order("salad", 6)
