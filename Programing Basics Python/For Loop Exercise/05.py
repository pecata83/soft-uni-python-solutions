number = int(input())

counts = [0, 0, 0, 0, 0]

for num in range(number):
    _input = int(input())

    if _input % 2 == 0:
        counts[0] += 1

    if _input % 3 == 0:
        counts[1] += 1

    if _input % 4 == 0:
        counts[2] += 1


print(f"{counts[0] / number * 100:.2f}%")
print(f"{counts[1] / number * 100:.2f}%")
print(f"{counts[2] / number * 100:.2f}%")
