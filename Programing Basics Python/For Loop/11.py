lily_age = int(input())
washingmachine_price = float(input())
single_toy_price = int(input())

money_sum = 0
last_bday_money = 0
brother_money = 0
toys_sum = 0

for bday in range(1, lily_age + 1):
    if bday % 2 == 0:
        last_bday_money += 10
        money_sum += last_bday_money
        brother_money += 1
    else:
        toys_sum += single_toy_price

total_money = (money_sum - brother_money) + toys_sum

if total_money >= washingmachine_price:
    print(f"Yes! {total_money - washingmachine_price:.2f}")
else:
    print(f"No! {abs(total_money - washingmachine_price):.2f}")
