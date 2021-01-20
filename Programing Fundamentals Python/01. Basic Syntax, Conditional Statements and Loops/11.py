fruit = input()
day_of_week = input()
quantity = float(input())

week_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
weekend_days = ["Saturday", "Sunday"]
price = 0

week_days_prices = {
    "banana": 2.5,
    "apple": 1.2,
    "orange": 0.85,
    "grapefruit": 1.45,
    "kiwi": 2.70,
    "pineapple": 5.50,
    "grapes": 3.85
}

weekend_prices = {
    "banana": 2.7,
    "apple": 1.25,
    "orange": 0.90,
    "grapefruit": 1.60,
    "kiwi": 3.00,
    "pineapple": 5.60,
    "grapes": 4.20
}


if day_of_week in week_days:

    if fruit in week_days_prices:
        price = week_days_prices[fruit] * quantity
        print(f'{price:.2f}')
    else:
        print(f'error')

elif day_of_week in weekend_days:

    if fruit in week_days_prices:
        price = weekend_prices[fruit] * quantity
        print(f'{price:.2f}')
    else:
        print(f'error')

else:
    print(f'error')
