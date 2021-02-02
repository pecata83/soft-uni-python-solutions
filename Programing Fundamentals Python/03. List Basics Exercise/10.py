INITIAL_ENERGIE, current_energie = 100, 100
INITIAL_COINS, current_coins = 100, 100
ENERGIE_NEEDED_PER_ORDER = 30
ENERGIE_GAINED_WHEN_TIRED = 50

events_stack = input().split("|")[::-1]

while events_stack:
    event, value = events_stack.pop().split("-")
    value = int(value)

    if event == "rest":
        energie = value

        if current_energie + energie > INITIAL_ENERGIE:
            energie = 100 - current_energie

        current_energie += energie
        print(f"You gained {energie} energy.")
        print(f"Current energy: {current_energie}.")

    elif event == "order":
        coins = value

        if current_energie - ENERGIE_NEEDED_PER_ORDER < 0:
            current_energie += ENERGIE_GAINED_WHEN_TIRED
            print("You had to rest!")
        else:
            current_energie -= ENERGIE_NEEDED_PER_ORDER
            current_coins += coins
            print(f"You earned {coins} coins.")

    else:
        ingredient = event
        expenses = value
        current_coins -= expenses

        if current_coins <= 0:
            print(f"Closed! Cannot afford {ingredient}.")
            events_stack.append(f"{event}-{value}")
            break
        else:
            print(f"You bought {ingredient}.")

if not events_stack:
    print(f"Day completed!")
    print(f"Coins: {current_coins}")
    print(f"Energy: {current_energie}")
