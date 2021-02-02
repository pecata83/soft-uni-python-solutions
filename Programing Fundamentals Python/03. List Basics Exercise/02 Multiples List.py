factor = int(input())
count = int(input())


factor_list = [i * factor for i in range(1, count + 1)]


# factor_list = []
# last_factor = 0

# for _ in range(0, count):
#     last_factor += factor
#     factor_list.append(last_factor)

print(factor_list)
