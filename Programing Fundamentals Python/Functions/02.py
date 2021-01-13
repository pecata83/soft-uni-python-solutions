input_operator = input()
first_num = int(input())
second_num = int(input())


def calculate(a, b, operator):

    if operator == "multiply":
        return a * b
    elif operator == "divide":
        return a / b
    elif operator == "add":
        return a + b
    elif operator == "subtract":
        return a - b


print(int(calculate(first_num, second_num, input_operator)))