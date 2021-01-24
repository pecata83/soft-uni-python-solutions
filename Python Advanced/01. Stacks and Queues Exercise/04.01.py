clothes_stack = [int(x) for x in input().split()]
rack_capacity = int(input())

current_rack_capacity = rack_capacity
racks_used = 1


while clothes_stack:
    cloth = clothes_stack.pop()

    if current_rack_capacity >= cloth:
        current_rack_capacity -= cloth
    else:
        racks_used += 1
        current_rack_capacity = rack_capacity - cloth


print(racks_used)
