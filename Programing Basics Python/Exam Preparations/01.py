number = int(input())

current = 0

for row in range(1, number + 1):
    for col in range(1, row+1):
        current += 1
        print(current, end=' ')
        if current == number:
            break

    if current == number:
        break
    print()
