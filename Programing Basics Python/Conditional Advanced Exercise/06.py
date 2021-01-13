first_number = int(input())
second_number = int(input())
operator = input()


if operator == "+":
    result = first_number + second_number
    number_type = ("odd", "even")[result % 2 == 0]

    print(f"{first_number} + {second_number} = {result} - {number_type}")

elif operator == "-":
    result = first_number - second_number
    number_type = ("odd", "even")[result % 2 == 0]

    print(f"{first_number} - {second_number} = {result} - {number_type}")

elif operator == "*":
    result = first_number * second_number
    number_type = ("odd", "even")[result % 2 == 0]

    print(f"{first_number} * {second_number} = {result} - {number_type}")

elif operator == "/":

    if second_number == 0:
        print(f"Cannot divide {first_number} by zero")
    else:
        result = first_number / second_number
        print(f"{first_number} / {second_number} = {result:.2f}")

elif operator == "%":

    if second_number == 0:
        print(f"Cannot divide {first_number} by zero")
    else:
        result = first_number % second_number
        print(f"{first_number} % {second_number} = {result}")
