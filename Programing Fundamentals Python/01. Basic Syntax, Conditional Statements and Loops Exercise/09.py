budget = float(input())
flour_price_per_kilo = float(input())

colored_egs = 0

egs_price_per_pack = flour_price_per_kilo * .75
milk_price_per_litre = flour_price_per_kilo * 1.25
milk_price_per_kozonak = milk_price_per_litre / 4

kozonak_price = flour_price_per_kilo + \
    egs_price_per_pack + milk_price_per_kozonak
kozonaks_made = int(budget // kozonak_price)
money_left = budget % kozonak_price

for k in range(1, kozonaks_made + 1):
    colored_egs += 3

    if k % 3 == 0:
        lost_egs = k - 2
        colored_egs -= lost_egs


print(f"You made {kozonaks_made} cozonacs! Now you have {colored_egs} eggs and {money_left:.2f}BGN left.")
