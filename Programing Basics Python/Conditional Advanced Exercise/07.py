month = input()
nights = int(input())

studio_price = 0
apartament_price = 0

if month == "May" or month == "October":
    studio_price = 50 * nights
    apartament_price = 65 * nights

    if 7 < nights <= 14:
        studio_price *= 0.95
    elif nights > 14:
        studio_price *= 0.7

elif month == "June" or month == "September":
    studio_price = 75.20 * nights
    apartament_price = 68.7 * nights

    if nights > 14:
        studio_price *= 0.8

elif month == "July" or month == "August":
    studio_price = 76 * nights
    apartament_price = 77 * nights


if nights > 14:
    apartament_price *= 0.9

print(f"Apartment: {apartament_price:.2f} lv.")
print(f"Studio: {studio_price:.2f} lv.")
