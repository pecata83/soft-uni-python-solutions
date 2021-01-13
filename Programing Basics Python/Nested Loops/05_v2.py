destination = input()

while destination != "End":

    holiday_price = int(input())
    money = 0

    while money < holiday_price:
        saved_money = int(input())
        money += saved_money
    else:
        print(f"Going to {destination}!")

    destination = input()
