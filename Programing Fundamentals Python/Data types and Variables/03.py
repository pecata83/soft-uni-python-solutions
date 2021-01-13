n = int(input())

for number in range(1, n + 1):
    sum_of_digits = 0

    number_copy = number
    while number_copy > 0:
        digit = number_copy % 10
        sum_of_digits += digit
        number_copy = int(number_copy / 10)

    is_special = False

    if sum_of_digits == 5 or sum_of_digits == 7 or sum_of_digits == 11:
        is_special = True

    print(f"{number} -> {is_special}")