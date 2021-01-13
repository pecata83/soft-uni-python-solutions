import math

holiday_price = float(input())

puzzles_number = int(input())
talking_doll_number = int(input())
teddy_bears_number = int(input())
minions_number = int(input())
trucks_number = int(input())

toys_number = puzzles_number + talking_doll_number + \
    teddy_bears_number + minions_number + trucks_number
toys_total_price = puzzles_number * 2.6 + talking_doll_number * 3 + \
    teddy_bears_number * 4.1 + minions_number * 8.2 + trucks_number * 2

if toys_number >= 50:
    toys_total_price = toys_total_price - (toys_total_price * 0.25)

price_after_expenses = toys_total_price - (toys_total_price * 0.1)

if price_after_expenses >= holiday_price:
    print(f'Yes! {(price_after_expenses - holiday_price):.2f} lv left.')

elif price_after_expenses < holiday_price:
    print(
        f'Not enough money! {abs(price_after_expenses - holiday_price):.2f} lv needed.')
