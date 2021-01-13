number = int(input())

counts = [0, 0, 0, 0, 0]

for num in range(number):
    _input = int(input())

    if _input < 200:
        counts[0] += 1

    elif _input <= 399:
        counts[1] += 1

    elif _input <= 599:
        counts[2] += 1

    elif _input <= 799:
        counts[3] += 1

    elif _input >= 800:
        counts[4] += 1


print(f"{counts[0] / number * 100:.2f}%")
print(f"{counts[1] / number * 100:.2f}%")
print(f"{counts[2] / number * 100:.2f}%")
print(f"{counts[3] / number * 100:.2f}%")
print(f"{counts[4] / number * 100:.2f}%")
