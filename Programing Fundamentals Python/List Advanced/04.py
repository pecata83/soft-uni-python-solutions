numbers_str = input()

numbers = numbers_str.split(", ")

indexes = [index for index, n in enumerate(numbers) if int(n) % 2 == 0]

print(indexes)
