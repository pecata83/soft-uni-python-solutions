from collections import deque

pumps_count = int(input())
queue = deque()

for _ in range(pumps_count):
    queue.append([int(x) for x in input().split()])

queue.rotate(1)
starting_pump = 0

for pump_index in range(pumps_count):
    is_starting_pump = True
    queue.rotate(-1)

    total_petrol = 0

    for petrol, distance in queue:
        total_petrol += petrol
        if total_petrol >= distance:
            total_petrol -= distance
        else:
            is_starting_pump = False
            break

    if is_starting_pump:
        starting_pump = pump_index
        break

print(starting_pump)
