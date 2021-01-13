factor = int(input())
count = int(input())

factor_list = []
last_factor = 0

for n in range(0, count):
    last_factor += factor
    factor_list.append(last_factor)

print(factor_list)