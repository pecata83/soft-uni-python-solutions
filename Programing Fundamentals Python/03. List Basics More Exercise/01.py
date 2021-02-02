zeros = []

numbers = list(map(int, input().split(", ")))

while 0 in numbers:
    zeros.append(0)
    numbers.remove(0)

print(numbers+zeros)


# numbers = [int(x) for x in input().split(", ")]

# queue = []

# for n in reversed(numbers):
#     if n == 0:
#         queue.insert(0, n)
#     else:
#         queue.append(n)

# print(list(queue)[::-1])


# from collections import deque

# numbers = [int(x) for x in input().split(", ")]

# queue = deque()

# for n in reversed(numbers):
#     if n == 0:
#         queue.appendleft(n)
#     else:
#         queue.append(n)

# print(list(queue)[::-1])


# zeros = []
# none_zeros = []

# for n in numbers:
#     if n == 0:
#         zeros.append(n)
#     else:
#         none_zeros.append(n)
