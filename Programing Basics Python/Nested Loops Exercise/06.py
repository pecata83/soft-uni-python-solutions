_input = int(input())

for num in range(1111, 10000):
    to_print = True

    for num_string_index in range(0, len(str(num))):
        num_string = str(num)[num_string_index]

        if int(num_string) == 0:
            to_print = False
            break
        elif _input % int(num_string) != 0:
            to_print = False
            break

    if to_print:
        print(num, end=" ")
