cards_string = input()
shuffles = int(input())

cards = cards_string.split()

for s in range(shuffles):
    middle_item = int(len(cards) / 2)
    first_half_cards = cards[0:middle_item]
    second_half_cards = cards[middle_item : int(len(cards))]
    cards = []
    for i in range(middle_item):
        cards.append(first_half_cards[i])
        cards.append(second_half_cards[i])

print(cards)