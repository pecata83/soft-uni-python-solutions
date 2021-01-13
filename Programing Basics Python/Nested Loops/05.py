while True:

    destination = input()

    if destination == "End":
        break

    holiday_price = float(input())

    while holiday_price > 0:
        saved_money = float(input())
        holiday_price -= saved_money
    else:
        print(f"Going to {destination}!")
