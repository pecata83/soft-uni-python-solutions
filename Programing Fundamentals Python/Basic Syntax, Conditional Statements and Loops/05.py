desired_size = int(input())
direction = 1
current_size = 0

while current_size < desired_size :
    current_size += 1
    print("*" * current_size)
    if desired_size == current_size:
        break


# number = int(input())
# for n in range(1, number + 1):
#     print("*" * n)

# for n in range(number - 1, -1, -1):
#     print("*" * n)
    

