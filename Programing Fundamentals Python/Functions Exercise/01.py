def get_smallest_number(numbers):
    numbers.sort()
    return numbers[0]


print(
    get_smallest_number([int(input()),
                         int(input()),
                         int(input())])
)
