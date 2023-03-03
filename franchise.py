from orderfactory import OrderFactory

class Franchise:

    def location_number(self) -> int :
        self.location_number = 1

    def place_order(self):
        oder_factory = OrderFactory()
        order = oder_factory.create_order("pizza")