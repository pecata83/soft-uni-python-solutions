import sys

iterations = int(input())

lowest_number = sys.maxsize
highest_number = -sys.maxsize

for i in range(iterations):
    value = int(input())

    if value < lowest_number:
        lowest_number = value

    if value > highest_number:
        highest_number = value


print(f"Max number: {highest_number}")
print(f"Min number: {lowest_number}")
