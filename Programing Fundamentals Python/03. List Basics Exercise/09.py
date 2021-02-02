MAX_PRICES = {
    "Clothes": 50,
    "Shoes": 35,
    "Accessories": 20.50
}

items = input().split("|")
budget = int(input())

initial_budget = budget

bought_items = []

for item in items:
    item_name, price = item.split("->")
    price = float(price)

    if price <= MAX_PRICES[item_name] and budget - price >= 0:
        bought_items.append(format(price * 1.4, ".2f"))
        budget -= price

sold_items_sum = sum([float(x) for x in bought_items])
profit = sold_items_sum - initial_budget + budget

print(" ".join(bought_items))
print(f"Profit: {profit:.2f}")

if initial_budget + profit >= 150:
    print("Hello, France!")
else:
    print("Time to go.")
