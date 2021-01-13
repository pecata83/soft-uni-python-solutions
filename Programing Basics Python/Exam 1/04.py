num_n = int(input())
num_m = int(input())
num_s = int(input())

for address in range(num_m, num_n - 1, -1):
    if address % 2 == 0 and address % 3 == 0:
        if address == num_s:
            break
        else:
            print(address, end=" ")
