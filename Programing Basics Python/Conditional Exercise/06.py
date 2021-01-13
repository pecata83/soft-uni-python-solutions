budget = float(input())
statists_count = int(input())
statists_dressup_price = float(input())

decour_price = budget * 0.1
total_statists_dressup_price = statists_count * statists_dressup_price

if statists_count > 150:
    total_statists_dressup_price *= 0.9

total_price = decour_price + total_statists_dressup_price

if total_price > budget:
    print("Not enough money!")
    print(f'Wingard needs {abs(budget - total_price):.2f} leva more.')

elif total_price <= budget:
    print("Action!")
    print(f'Wingard starts filming with {budget - total_price:.2f} leva left.')
