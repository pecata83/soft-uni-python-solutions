divisor = int(input())
bound = int(input())

largest_divisor = 0

for n in range(divisor, bound + 1):
    if 0 < n <= bound and n % divisor == 0:
        largest_divisor = n

print(largest_divisor)