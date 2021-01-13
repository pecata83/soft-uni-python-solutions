width = int(input())
length = int(input())
height = int(input())

available_free_space = width * height * length
boxes_space_needed = 0

command = input()

while command != "Done":
    command_number = int(command)
    boxes_space_needed += command_number

    if available_free_space >= boxes_space_needed:
        command = input()
    else:
        print(
            f"No more free space! You need {boxes_space_needed - available_free_space} Cubic meters more.")
        break

else:
    print(f"{available_free_space - boxes_space_needed} Cubic meters left.")
