import sys

number = int(input())

max_num = -sys.maxsize
numbers_sum = 0

for i in range(number):

    _input = int(input())

    if _input > max_num:
        max_num = _input

    numbers_sum += _input

if max_num == numbers_sum - max_num:
    print("Yes")
    print(f"Sum = {max_num}")
else:
    print("No")
    print(f"Diff = {abs(max_num - (numbers_sum - max_num))}")
