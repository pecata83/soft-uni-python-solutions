open_tabs = int(input())
salary = float(input())

for tab in range(1, open_tabs + 1):
    _input = input()

    if _input == "Facebook":
        salary -= 150
    elif _input == "Instagram":
        salary -= 100
    elif _input == "Reddit":
        salary -= 50

    if salary <= 0:
        print("You have lost your salary.")
        break


if salary > 0:
    print(int(salary))
