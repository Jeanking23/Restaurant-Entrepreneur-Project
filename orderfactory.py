from pizza import Pizza
from pasta import Pasta
from salad import Salad
class OrderFactory:

    def create_order(self, dish_name):
        if dish_name == "pizza":
            return Pizza()
        elif dish_name == "pasta":
            return Pasta()
        elif dish_name == "salad":
            return Salad()