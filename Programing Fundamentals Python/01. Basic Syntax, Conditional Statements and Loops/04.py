MIN_NUMBER = 1
MAX_NUMBER = 100

number = float(input())

while  number < MIN_NUMBER or number > MAX_NUMBER:
    number = float(input())

print(f"The number {number} is between {MIN_NUMBER} and {MAX_NUMBER}")