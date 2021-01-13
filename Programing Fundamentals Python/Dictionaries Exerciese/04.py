class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def set_quantity(self, quantity):
        self.quantity += quantity

    def set_price(self, price):
        self.price = price


class Store:
    def __init__(self, name):
        self.name = name
        self.products = {}

    def add_product(self, new_product):
        if new_product.name in self.products:
            product = new_product.name
            self.products[product].set_price(new_product.price)
            self.products[product].set_quantity(new_product.quantity)
        else:
            self.products[new_product.name] = new_product

    def __repr__(self):
        return "\n".join(self.products.items())

    def buy(self):
        for key, product in self.products.items():
            total_price = product.price * product.quantity
            print(product.name, "->", format(total_price, ".2f"))


my_store = Store("my_store")

while True:
    command = input()

    if command == "buy":
        my_store.buy()
        break

    name, price, quantity = command.split()

    product = Product(name, float(price), int(quantity))

    my_store.add_product(product)
