width = int(input())
length = int(input())

cake_peaces = width * length

while True:
    if cake_peaces >= 0:

        _input = input()

        if _input == "STOP":
            print(f"{cake_peaces} pieces are left.")
            break
        else:
            cake_peaces -= int(_input)

    else:
        print(f"No more cake left! You need {abs(cake_peaces)} pieces more.")
        break
