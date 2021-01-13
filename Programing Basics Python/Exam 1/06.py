locations_number = int(input())

for location in range(locations_number):

    expected_average_gold_per_day = float(input())
    mining_days_on_location = int(input())
    gold_mined_on_location = 0

    for mining_day in range(mining_days_on_location):
        gold_mined_on_location += float(input())

    average_gold_per_day = gold_mined_on_location / mining_days_on_location

    if average_gold_per_day >= expected_average_gold_per_day:
        print(f"Good job! Average gold per day: {average_gold_per_day:.2f}.")
    else:
        print(
            f"You need {expected_average_gold_per_day - average_gold_per_day:.2f} gold.")
