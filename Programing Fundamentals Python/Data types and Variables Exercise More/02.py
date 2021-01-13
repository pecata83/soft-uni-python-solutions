num1 = int(input())
num2 = int(input())

is_normal = True

while True:
    if is_normal:
        print("Before:")
        print(f"a = {num1}")
        print(f"b = {num2}")
        is_normal = False

    else:
        print("After:")
        print(f"a = {num2}")
        print(f"b = {num1}")
        break
