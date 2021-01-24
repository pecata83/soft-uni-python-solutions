ORNAMENT_SET_PRICE = 2
TREE_SKIRT_PRICE = 5
TREE_GARLANDS_PRICE = 3
TREE_LIGHTS_PRICE = 15

ornament_max_quantity = int(input())
days = int(input())

christmas_spirit = 0

ornament_quantities = {
    "ornament_set": 0,
    "tree_skirt": 0,
    "tree_garlands": 0,
    "tree_lights": 0
}

for day in range(1, days+1):

    if day % 11 == 0:
        ornament_max_quantity += 2

    if day % 2 == 0:
        ornament_quantities["ornament_set"] += ornament_max_quantity
        christmas_spirit += 5

    if day % 3 == 0:
        ornament_quantities["tree_skirt"] += ornament_max_quantity
        ornament_quantities["tree_garlands"] += ornament_max_quantity
        christmas_spirit += 13

    if day % 5 == 0:
        ornament_quantities["tree_lights"] += ornament_max_quantity
        christmas_spirit += 17

    if day % 5 == 0 and day % 3 == 0:
        christmas_spirit += 30

    if day % 10 == 0:
        christmas_spirit -= 20
        ornament_quantities["tree_skirt"] += 1
        ornament_quantities["tree_garlands"] += 1
        ornament_quantities["tree_lights"] += 1

    if day % 10 == 0 and day == days:
        christmas_spirit -= 30


total_price = ornament_quantities["ornament_set"] * ORNAMENT_SET_PRICE + \
    ornament_quantities["tree_skirt"] * TREE_SKIRT_PRICE + \
    ornament_quantities["tree_garlands"] * TREE_GARLANDS_PRICE + \
    ornament_quantities["tree_lights"] * TREE_LIGHTS_PRICE

print(f"Total cost: {total_price}")
print(f"Total spirit: {christmas_spirit}")
