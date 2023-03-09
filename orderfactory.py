from pizza import Pizza
from pasta import Pasta
from salad import Salad
class OrderFactory:
    @staticmethod
    def create_order(dish_name, price):
        if dish_name == "pizza":
            return Pizza(dish_name, price)
        elif dish_name == "pasta":
            return Pasta(dish_name, price)
        elif dish_name == "salad":
            return Salad(dish_name, price)
        else :
             print(f"Invalid dish name: {dish_name}")
