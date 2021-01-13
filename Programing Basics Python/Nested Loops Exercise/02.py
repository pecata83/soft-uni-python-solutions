num1 = int(input())
num2 = int(input())

for n in range(num1, num2 + 1):
    even_sum = 0
    odd_sum = 0
    for index, digit in enumerate(str(n)):
        if index % 2 == 0:
            even_sum += int(digit)
        elif index % 2 == 1:
            odd_sum += int(digit)

    if even_sum == odd_sum:
        print(n, end=' ')
