string = input()

numbers = string.split()
turned_numbers = []

for n in numbers:
    number = int(n) * -1
    # converted_number = number * -1
    turned_numbers.append(number)

print(turned_numbers)