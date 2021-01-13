steps_goal = 10000
steps_made = 0
going_home = False

while True:

    if steps_made >= steps_goal:
        print("Goal reached! Good job!")
        print(f"{abs(steps_made - steps_goal)} steps over the goal!")
        break

    _input = input()

    if _input == "Going home":
        going_home = True
        continue

    elif going_home == True:
        steps_made += int(_input)

        steps_difference = steps_made - steps_goal

        if steps_difference >= 0:
            print("Goal reached! Good job!")
            print(f"{abs(steps_difference)} steps over the goal!")
            break
        else:
            print(f"{abs(steps_difference)} more steps to reach goal.")
            break

    else:
        steps_made += int(_input)
