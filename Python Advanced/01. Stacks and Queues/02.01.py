expression = list(input())

opening_brackets_stack = []

brackets_list = []

for i, c in enumerate(expression):

    if c == "(":
        opening_brackets_stack.append(i)

    if c == ")":
        brackets_list.append([opening_brackets_stack.pop(), i+1])

for b1, b2 in brackets_list:
    bracket = expression[b1:b2]
    print("".join(bracket))
