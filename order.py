class Order:

    def __init__(self):
        self.dish.name = " "
        self.price = 0

#create a child class  menu of pizza, pasta, salad and their prices
class pizza(Order):
    def __init__(self):
        super().__init__()
        self.dish_name = "pizza"
        self.price = 10

class pasta(Order):
    def __init__(self):
        super().__init__()
        self.dish_name = "pasta"
        self.price = 5

class salad(Order):
    def __init__(self):
        super().__init__()
        self.dish_name = "salad"
        self.price = 20