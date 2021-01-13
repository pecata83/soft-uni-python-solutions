num = int(input())

even_numbers = []
odd_numbers = []
negative_numbers = []
positive_numbers = []

for _ in range(num):
    entry_number = int(input())

    if entry_number % 2 == 0:
        even_numbers.append(entry_number)

    if entry_number % 2 != 0:
        odd_numbers.append(entry_number)

    if entry_number < 0:
        negative_numbers.append(entry_number)

    if entry_number >= 0:
        positive_numbers.append(entry_number)

number_type = input()

if number_type == "even":
    print(even_numbers)

if number_type == "odd":
    print(odd_numbers)

if number_type == "negative":
    print(negative_numbers)

if number_type == "positive":
    print(positive_numbers)
