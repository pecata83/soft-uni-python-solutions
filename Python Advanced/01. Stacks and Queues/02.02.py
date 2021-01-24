expression = list(input())

brackets_stack = []


for c in expression:

    if c == "(":
        brackets_stack.append("")

    for index in range(len(brackets_stack)):
        brackets_stack[index] += c

    if c == ")":
        print(brackets_stack.pop())
