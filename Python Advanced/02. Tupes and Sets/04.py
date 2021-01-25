from collections import deque

water_quantity = int(input())

people = deque()

while True:
    command = input()

    if command == "Start":
        break
    else:
        name = command
        people.append(name)

while True:
    tokens = input().split(" ")

    if tokens[0] == "End":
        break

    if tokens[0] == "refill":
        water_quantity += int(tokens[1])
    else:
        litres_to_drink = int(tokens[0])

        if water_quantity - litres_to_drink >= 0:
            water_quantity -= litres_to_drink
            print(f"{people.popleft()} got water")
        else:
            print(f"{people.popleft()} must wait")


print(f"{water_quantity} liters left")
