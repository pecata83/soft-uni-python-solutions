elements = input().split()

bakery = {}

for e in range(0, len(elements), 2):
    bakery[elements[e]] = int(elements[e + 1])

print(bakery)
