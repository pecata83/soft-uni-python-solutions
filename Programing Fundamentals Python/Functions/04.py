prices = {"coffee": 1.50, "water": 1.00, "coke": 1.40, "snacks": 2.00}


def calculate_order(product: str, amount: int):
    return prices[product] * amount


product = input()
amount = int(input())

print(f"{calculate_order(product, amount):.2f}")