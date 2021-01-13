numbers_string = input()
numbers_to_remove = int(input())

numbers = [int(x) for x in numbers_string.split()]

sorted_numbers = sorted(numbers)

for n in range(numbers_to_remove):
    numbers.remove(sorted_numbers[n])

print(numbers)