import sys

number = int(input())

odd_sum = 0
odd_min = sys.maxsize
odd_max = -sys.maxsize

even_sum = 0
even_min = sys.maxsize
even_max = -sys.maxsize

for num in range(1, number + 1):

    _input = float(input())

    if num % 2 != 0:
        odd_sum += _input

        if odd_max < _input:
            odd_max = _input
        if odd_min > _input:
            odd_min = _input
    else:
        even_sum += _input

        if even_max < _input:
            even_max = _input
        if even_min > _input:
            even_min = _input

print(f"OddSum={odd_sum:.2f},")

if odd_min == sys.maxsize:
    print(f"OddMin=No,")
else:
    print(f"OddMin={odd_min:.2f},")

if odd_max == -sys.maxsize:
    print(f"OddMax=No,")
else:
    print(f"OddMax={odd_max:.2f},")

print(f"EvenSum={even_sum:.2f},")

if even_min == sys.maxsize:
    print(f"EvenMin=No,")
else:
    print(f"EvenMin={even_min:.2f},")

if even_max == -sys.maxsize:
    print(f"EvenMax=No")
else:
    print(f"EvenMax={even_max:.2f}")
