def get_even_and_odd_numbers(num: int):
    even_sum = 0
    odd_sum = 0

    num_string = str(num)

    for char in num_string:

        _i = int(char)

        if _i % 2 == 0:
            even_sum += int(char)
        elif _i % 2 != 0:
            odd_sum += int(char)

    return f"Odd sum = {odd_sum}, Even sum = {even_sum}"


output = get_even_and_odd_numbers(int(input()))
print(output)
