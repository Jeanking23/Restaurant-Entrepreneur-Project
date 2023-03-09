from order import Order

class Pasta(Order):
    def __init__(self, dish_name, price):
        super().__init__()
        self.dish_name = dish_name
        self.price = price
    
    def create_order(self):
        return f"{self.dish_name} pasta ordered for {self.price}$"
