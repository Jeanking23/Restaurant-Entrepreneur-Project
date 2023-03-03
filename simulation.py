from franchise import Franchise
from logger import Logger



class Simulation:
    def __init__(self):
        self.franchise = Franchise()
        self.logger = Logger()

    def run_simulation(self, price) :
        self.franchise.place_order()
        self.logger.log_transaction("pizza", price)


