iterations = int(input())

lowest_number = 0
highest_number = 0

for i in range(iterations):
    value = int(input())
    if i == 0:
        lowest_number = value
        highest_number = value

    if value < lowest_number:
        lowest_number = value

    if value > highest_number:
        highest_number = value


print(f"Max number: {highest_number}")
print(f"Min number: {lowest_number}")
