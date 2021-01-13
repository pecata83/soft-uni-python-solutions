budget = float(input())
season = input()

destination = ""
accommodation_type = ""
percentage_spend = 0

if budget <= 100:

    destination = "Bulgaria"

    if season == "summer":
        percentage_spend = 0.3
        accommodation_type = "Camp"

    elif season == "winter":
        percentage_spend = 0.7
        accommodation_type = "Hotel"

elif budget <= 1000:

    destination = "Balkans"

    if season == "summer":
        percentage_spend = 0.4
        accommodation_type = "Camp"

    elif season == "winter":
        percentage_spend = 0.8
        accommodation_type = "Hotel"

elif budget > 1000:
    destination = "Europe"
    accommodation_type = "Hotel"
    percentage_spend = 0.9


print(f"Somewhere in {destination}")
print(f"{accommodation_type} - {budget * percentage_spend:.2f}")
