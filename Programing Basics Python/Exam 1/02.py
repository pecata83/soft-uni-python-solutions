from math import floor
spaceship_width = float(input())
spaceship_length = float(input())
spaceship_height = float(input())
austronaughts_average_height = float(input())

spaceship_volume = spaceship_width * spaceship_length * spaceship_height
astronaut_room_volume = (austronaughts_average_height + 0.4) * 2 * 2

persons_possible = floor(spaceship_volume / astronaut_room_volume)

if 3 <= persons_possible <= 10:
    print(f"The spacecraft holds {persons_possible} astronauts.")
elif persons_possible < 3:
    print("The spacecraft is too small.")
elif persons_possible > 10:
    print("The spacecraft is too big.")
