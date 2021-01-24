n = int(input())

sum_one = 0
sum_two = 0

for i in range(n):
    value = int(input())
    sum_one += value

for i in range(n):
    value = int(input())
    sum_two += value


if sum_one == sum_two:
    print(f"Yes, sum = {sum_one}")
elif sum_one != sum_two:
    print(f"No, diff = {abs(sum_one - sum_two)}")
