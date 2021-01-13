change = float(input())

change_in_cents = int(change * 100)

coins_count = 0

# Coins in cents = 200 , 100, 50, 20, 10, 5, 2, 1


def get_coins_count(change, coin):
    if change % coin != 0:
        return change_in_cents // coin
    else:
        return change_in_cents / coin


def get_remaining_change(change, coin):
    return change % coin


while change_in_cents != 0:

    if change_in_cents >= 200:
        coins_count += get_coins_count(change_in_cents, 200)
        change_in_cents = get_remaining_change(change_in_cents, 200)

    elif change_in_cents >= 100:
        coins_count += get_coins_count(change_in_cents, 100)
        change_in_cents = get_remaining_change(change_in_cents, 100)

    elif change_in_cents >= 50:
        coins_count += get_coins_count(change_in_cents, 50)
        change_in_cents = get_remaining_change(change_in_cents, 50)

    elif change_in_cents >= 20:
        coins_count += get_coins_count(change_in_cents, 20)
        change_in_cents = get_remaining_change(change_in_cents, 20)

    elif change_in_cents >= 10:
        coins_count += get_coins_count(change_in_cents, 10)
        change_in_cents = get_remaining_change(change_in_cents, 10)

    elif change_in_cents >= 5:
        coins_count += get_coins_count(change_in_cents, 5)
        change_in_cents = get_remaining_change(change_in_cents, 5)

    elif change_in_cents >= 2:
        coins_count += get_coins_count(change_in_cents, 2)
        change_in_cents = get_remaining_change(change_in_cents, 2)

    elif change_in_cents >= 1:
        coins_count += get_coins_count(change_in_cents, 1)
        change_in_cents = get_remaining_change(change_in_cents, 1)


print(f"{coins_count:.0f}")
