group_budget = int(input())
season = input()
fishermens_count = int(input())

price_by_season = {
    "Spring": 3000,
    "Summer": 4200,
    "Autumn": 4200,
    "Winter": 2600
}

discount = 0

if fishermens_count <= 6:
    discount = 0.9

elif 7 <= fishermens_count <= 11:
    discount = 0.85

elif fishermens_count >= 12:
    discount = 0.75

trip_price = price_by_season[season] * discount

if fishermens_count % 2 == 0 and season != "Autumn":
    trip_price = trip_price * 0.95

if trip_price <= group_budget:
    print(f"Yes! You have {group_budget - trip_price:.2f} leva left.")
elif trip_price > group_budget:
    print(
        f"Not enough money! You need {abs(group_budget - trip_price):.2f} leva.")
