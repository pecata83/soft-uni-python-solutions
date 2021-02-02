queue = input().split()
step = int(input())

result = []

while queue:
    if len(queue) < step:

    first_slice = queue[0:step]
    second_slice = queue[step::]
    queue = second_slice + first_slice
    result.append(queue.pop())


print(f"[{','.join(result)}]")

# from collections import deque

# queue = deque(input().split())
# step = int(input())

# result = []

# while queue:
#     queue.rotate(-step)
#     result.append(queue.pop())

# print(f"[{','.join(result)}]")
