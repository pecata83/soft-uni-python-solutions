dog_food_bought = int(input())
dog_food_in_grams = dog_food_bought * 1000
total_food_needed = 0

command = input()

while command != "Adopted":
    total_food_needed += int(command)
    command = input()
    # meal_in_grams = int(command)
else:
    leftover_food = dog_food_in_grams - total_food_needed

    if leftover_food >= 0:
        print(f"Food is enough! Leftovers: {leftover_food} grams.")
    else:
        print(f"Food is not enough. You need {abs(leftover_food)} grams more.")
