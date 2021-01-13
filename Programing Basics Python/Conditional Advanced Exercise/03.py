flower_type = input()
flower_count = int(input())
budget = int(input())

flowers_prices = {
    "Roses": 5,
    "Dahlias": 3.8,
    "Tulips": 2.8,
    "Narcissus": 3,
    "Gladiolus": 2.5
}

money_left = 0
total_price = flower_count * flowers_prices[flower_type]

if flower_type == "Roses":
    if flower_count > 80:
        total_price = total_price * 0.9

elif flower_type == "Dahlias":
    if flower_count > 90:
        total_price = total_price * 0.85

elif flower_type == "Tulips":
    if flower_count > 80:
        total_price = total_price * 0.85

elif flower_type == "Narcissus":
    if flower_count < 120:
        total_price = total_price * 1.15

elif flower_type == "Gladiolus":
    if flower_count < 80:
        total_price = total_price * 1.2


money_left = budget - total_price

if money_left >= 0:
    print(
        f"Hey, you have a great garden with {flower_count} {flower_type} and {money_left:.2f} leva left.")
elif money_left < 0:
    print(f"Not enough money, you need {abs(money_left):.2f} leva more.")
