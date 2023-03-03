class Logger:
    def __init__(self):
        self.transaction_count = 0
        self.daily_sales = 0

    def log_transaction(self, order, dish_name, price):
        self.dish_name = dish_name
        self.price
        with open("log.txt", "w") as f:
            f.write(f"Order: {order.dish_name}\nPrice: {price}\n\n")
            f.close()

        self.transaction_count += 1
        self.daily_sale += price
