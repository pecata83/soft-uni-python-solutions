floors = int(input())
apartaments = int(input())

for f in range(floors, 0, -1):
    floor_string = ""
    for a in range(apartaments):

        if f == floors:
            floor_string += f"L{f}{a} "
        elif f % 2 == 0:
            floor_string += f"O{f}{a} "
        elif f % 2 == 1:
            floor_string += f"A{f}{a} "

    print(floor_string)
