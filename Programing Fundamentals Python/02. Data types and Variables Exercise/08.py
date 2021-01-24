EARNINGS_PER_DAY = 50
PERSON_FOOD_PER_DAY_PRICE = 2
MOTIVATION_DAY_WATER_PRICE = 3
SLAYED_MONSTER_BONUS = 20
ADDITIONAL_SLAYED_MONSTER_MOTIVATION_PARTY_PRICE = 2

party_size = int(input())
days = int(input())

total_budget = 0
rations_price = 0
every_third_day_motivational_party_price = 0
boss_monster_motivational_party_same_day_price = 0
every_fifth_day_boss_monster_reward = 0

for day in range(1, days + 1):

    # Every 10th day 2 companions leave
    if day % 10 == 0:
        party_size -= 2

    # Every 15th day 5 companions join
    if day % 15 == 0:
        party_size += 5

    total_budget += EARNINGS_PER_DAY
    rations_price += party_size * PERSON_FOOD_PER_DAY_PRICE

    # Check if it is the third day
    if day % 3 == 0:
        # Calculate every third day motivational party costs
        every_third_day_motivational_party_price += (
            party_size * MOTIVATION_DAY_WATER_PRICE
        )

    # Check if it is the fifth day
    if day % 5 == 0:
        every_fifth_day_boss_monster_reward += party_size * SLAYED_MONSTER_BONUS

    # Check if its motivation and monster day
    if day % 3 == 0 and day % 5 == 0:
        boss_monster_motivational_party_same_day_price += (
            party_size * ADDITIONAL_SLAYED_MONSTER_MOTIVATION_PARTY_PRICE
        )


end_budget = (
    total_budget
    + every_fifth_day_boss_monster_reward
    - rations_price
    - every_third_day_motivational_party_price
    - boss_monster_motivational_party_same_day_price
)

print(f"{party_size} companions received {int(end_budget / party_size)} coins each.")