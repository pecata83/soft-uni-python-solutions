def get_factorial(num):
    result = num

    for n in range(num - 1, 1, -1):
        result *= n

    return result


def get_number(num1: int, num2: int):

    factorial1 = get_factorial(num1)
    factorial2 = get_factorial(num2)

    _result = factorial1 / factorial2
    return f"{_result:.2f}"


result = get_number(int(input()), int(input()))

print(result)
