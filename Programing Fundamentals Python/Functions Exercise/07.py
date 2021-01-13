def is_number_perfect(num: int):
    half_sum = int(num / 2)

    dividers = []

    for n in range(1, half_sum + 1):
        if num % n == 0:
            dividers.append(n)

    if sum(dividers) == num:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."


number = int(input())
result = is_number_perfect(number)

print(result)
