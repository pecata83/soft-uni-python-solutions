def remove_gift(gifts, gift):
    while gift in gifts:
        gifts[gifts.index(gift)] = None


def replace_gift(gifts, gift, index):
    if index < len(gifts) and index >= 0:
        gifts[index] = gift


gifts = input().split()

while True:
    tokens = input()

    if tokens == "No Money":
        break

    commands = tokens.split()
    command = commands[0]
    gift = commands[1]

    if command == "OutOfStock":
        remove_gift(gifts, gift)

    if command == "Required":
        index = int(commands[2])
        replace_gift(gifts, gift, index)

    if command == "JustInCase":
        gifts[-1] = gift

print(" ".join([x for x in gifts if x is not None]))

#########################################
# Alternative version without functions #
#########################################
# gifts_string = input()
# possible_gifts = gifts_string.split()

# while True:
#     commands = input().split()
#     command = commands[0]

#     if command == "OutOfStock":
#         gift_name = commands[1]

#         if gift_name in possible_gifts:

#             for i, gift in enumerate(possible_gifts):

#                 if gift == gift_name:
#                     possible_gifts[i] = "None"

#     elif command == "Required":
#         gift_name = commands[1]
#         gift_index = int(commands[2])

#         if gift_index < len(possible_gifts) and gift_index >= 0:
#             possible_gifts[gift_index] = gift_name

#     elif command == "JustInCase":
#         gift_name = commands[1]

#         possible_gifts[-1] = gift_name

#     elif command == "No" and commands[1] == "Money":
#         break


# final_gift_list = []

# for gift in possible_gifts:
#     if gift != "None":
#         final_gift_list.append(gift)

# print(" ".join(final_gift_list))
