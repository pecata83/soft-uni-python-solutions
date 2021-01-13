elements = input().split()
searched_products = input().split()

bakery = {}

for e in range(0, len(elements), 2):
    bakery[elements[e]] = int(elements[e + 1])


for product in searched_products:
    if product in bakery:
        print(f"We have {bakery[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")
