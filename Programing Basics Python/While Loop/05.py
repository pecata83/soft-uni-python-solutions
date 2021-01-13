account_sum = 0

while True:
    amount = input()

    if amount == "NoMoreMoney":
        break
    else:
        _amount = float(amount)

        if _amount >= 0:
            account_sum += _amount
            print(f"Increase: {_amount:.2f} ")
        else:
            print(f"Invalid operation!")
            break

print(f"Total: {account_sum:.2f}")
