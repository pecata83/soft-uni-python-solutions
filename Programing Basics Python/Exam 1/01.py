import math

distance_to_moon = 384400

average_speed = float(input())
fuel_per_hundred_km_needed = float(input())

hours_needed = (distance_to_moon / average_speed * 2) + 3
fuel_needed = (distance_to_moon / 100 * fuel_per_hundred_km_needed) * 2


print(int(math.ceil(hours_needed)))
print(int(fuel_needed))
