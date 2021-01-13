def get_middle_char(text):
    text_list = text.split()
    middle_char_index = len(text_list) // 2
    middle_char = text_list[middle_char_index]
    return middle_char


def split_text_by_middle_char(text):
    return text.split(f" {get_middle_char(text)} ")


def print_side(side, members):
    '''DOC STRING'''
    print(f"Side: {side}, Members: {len(members)}")
    for member in members.keys():
        print("!", member)


force = {}
sides = {}

command = input()

while command != "Lumpawaroo":
    middle_sign = get_middle_char(command)

    if middle_sign == "|":
        force_side, force_user = split_text_by_middle_char(command)

        if force_side not in sides and len(sides) < 2:
            sides[force_side] = {}

        if force_user not in force and force_side in sides:
            force[force_user] = force_side
        elif force_side in sides:
            force[force_user] = force_side

    elif middle_sign == "->":
        force_user, force_side = split_text_by_middle_char(command)

        if force_side not in sides and len(sides) < 2:
            sides[force_side] = {}

        if force_user not in force and force_side in sides:
            force[force_user] = force_side
        elif force_side in sides:
            force[force_user] = force_side

        print(f"{force_user} joins the {force_side} side!")

    command = input()

for side in sides.keys():
    filtered_force = dict(filter(lambda x: x[1] == side, force.items()))
    sorted_filtered_force = dict(
        sorted(filtered_force.items(), key=lambda x: x[0]))
    sides[side] = sorted_filtered_force


sorted_sides = dict(
    sorted(sides.items(), key=lambda x: (-len(x[1]), x[0]), reverse=False)
)

for side, force_users in sorted_sides.items():
    if len(force_users) > 0:
        print_side(side, force_users)

# print(sorted_sides)
