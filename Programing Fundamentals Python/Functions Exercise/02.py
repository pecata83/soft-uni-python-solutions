n1 = int(input())
n2 = int(input())
n3 = int(input())


def sum_numbers(_n1: int, _n2: int):
    return _n1 + _n2


def subtract(_n1: int, _n2: int):
    return _n1 - _n2


def add_and_subtrack(_n1: int, _n2: int, _n3: int):

    summed_number = sum_numbers(_n1, _n2)
    subtracted_number = subtract(summed_number, _n3)

    return subtracted_number


print(add_and_subtrack(n1, n2, n3))
