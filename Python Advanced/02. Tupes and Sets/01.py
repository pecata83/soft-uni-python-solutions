numbers = tuple(map(float, input().split()))

checked_values = set()

for n in numbers:
    if n not in checked_values:
        checked_values.add(n)
        print(f"{n} - {numbers.count(n)} times")
