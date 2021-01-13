rooms = int(input())

total_seats = 0
total_people = 0
is_enough = True

for number_of_room in range(1, rooms + 1):
    tokens = input().split()
    seats = len(tokens[0])
    people = int(tokens[1])

    total_seats += seats
    total_people += people

    if people > seats:
        is_enough = False
        needed_chairs_in_room = abs(people - seats)
        print(f"{needed_chairs_in_room} more chairs needed in room {number_of_room}")

total_free_chairs = total_seats - total_people

if is_enough:
    print(f"Game On, {total_free_chairs} free chairs left")
