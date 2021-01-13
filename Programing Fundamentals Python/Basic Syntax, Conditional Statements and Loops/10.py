n = int(input())

sum_even = 0
sum_odd = 0

for i in range(n):
    value = int(input())

    if i % 2 == 0:
        sum_even += value
    else:
        sum_odd += value

if sum_even == sum_odd:
    print(f"Yes")
    print(f"Sum = {sum_even}")
elif sum_even != sum_odd:
    print(f"No")
    print(f"Diff = {abs(sum_even - sum_odd)}")
