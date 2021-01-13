excursion_price = float(input())
available_money = float(input())
continues_days_spending = 0
total_days = 0

while True:

    if continues_days_spending == 5:
        print("You can't save the money.")
        print(total_days)
        break

    if available_money >= excursion_price:
        print(f"You saved the money for {total_days} days.")
        break

    action_type = input()
    amount = float(input())
    total_days += 1

    if action_type == "spend":
        available_money -= amount
        if available_money < 0:
            available_money = 0

        continues_days_spending += 1

    elif action_type == "save":
        available_money += amount
        continues_days_spending = 0
