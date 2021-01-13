city = input()
amount = float(input())

commissions = {
    "low": {
        "Sofia": 5,
        "Varna": 4.5,
        "Plovdiv": 5.5
    },
    "med": {
        "Sofia": 7,
        "Varna": 7.5,
        "Plovdiv": 8
    },
    "high": {
        "Sofia": 8,
        "Varna": 10,
        "Plovdiv": 12
    },
    "max": {
        "Sofia": 12,
        "Varna": 13,
        "Plovdiv": 14.5
    },
}

if 0 <= amount <= 500:
    if city in commissions["low"]:
        commission = (amount / 100 * commissions["low"][city])
        print(f'{commission:.2f}')
    else:
        print("error")
elif 500 < amount <= 1000:
    if city in commissions["med"]:
        commission = (amount / 100 * commissions["med"][city])
        print(f'{commission:.2f}')
    else:
        print("error")
elif 1000 < amount <= 10000:
    if city in commissions["high"]:
        commission = (amount / 100 * commissions["high"][city])
        print(f'{commission:.2f}')
    else:
        print("error")
elif amount > 1000:
    if city in commissions["max"]:
        commission = (amount / 100 * commissions["max"][city])
        print(f'{commission:.2f}')
    else:
        print("error")
else:
    print("error")
