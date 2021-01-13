TANK_CAPACITY = 255

times = int(input())

poured_water = 0

for t in range(0, times):
    liters = int(input())

    if poured_water + liters <= TANK_CAPACITY:
        poured_water += liters
    else:
        print("Insufficient capacity!")

print(poured_water)
