from order import Order
class Pizza :

  class pizza(Order):
    def __init__(self):
        super().__init__()
        self.dish_name = "pizza"
        self.price = 10