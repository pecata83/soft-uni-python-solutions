import sys

command = input()

min_num = sys.maxsize

while command != "Stop":

    number = int(command)

    if number < min_num:
        min_num = number
    command = input()

else:

    print(f"{min_num}")
