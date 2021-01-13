lost_fight_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

broken_helmet_count = 0
broken_sword_count = 0
broken_shield_count = 0
broken_armor_count = 0

for lost_fight in range(1, lost_fight_count + 1):
    broken_helmet = False
    broken_sword = False
    broken_shield = False
    broken_armor = False

    if lost_fight % 2 == 0:
        broken_helmet = True
        broken_helmet_count += 1

    if lost_fight % 3 == 0:
        broken_sword = True
        broken_sword_count += 1

    if broken_helmet and broken_sword:
        broken_shield = True
        broken_shield_count += 1

    if broken_shield and broken_shield_count % 2 == 0:
        broken_armor = True
        broken_armor_count += 1

expenses = (
    broken_helmet_count * helmet_price
    + broken_sword_count * sword_price
    + broken_shield_count * shield_price
    + broken_armor_count * armor_price
)

print(f"Gladiator expenses: {expenses:.2f} aureus")