from collections import deque

food_quantity = int(input())
orders = deque([int(x) for x in input().split()])

max_order = max(orders)

for _ in range(len(orders)):
    order = orders.popleft()

    if food_quantity >= order:
        food_quantity -= order
    else:
        orders.appendleft(order)
        break
        # OR WE CAN APPEND ORDER TO THE END OF THE QUEUE AND PROCEED WITH THE NEXT POSSIBLE ORDER?
        # orders.append(order)

print(max_order)

if len(orders) > 0:
    print(f"Orders left: {' '.join(str(x) for x in orders)}")
else:
    print("Orders complete")
