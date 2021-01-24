number = int(input())

stack = []

for _ in range(number):
    tokens = [int(x) for x in input().split()]
    action_type = tokens[0]

    if action_type == 1:
        element = tokens[1]
        stack.append(element)
    elif action_type == 2:
        if len(stack) > 0:
            stack.pop()
    elif action_type == 3:
        if stack:
            print(max(stack))
    elif action_type == 4:
        if stack:
            print(min(stack))


print(", ".join(str(x) for x in stack[::-1]))
