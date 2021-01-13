days = int(input())
accommodation_type = input()
grade = input()

room_for_one_person_price = 18.00
apartment_price = 25.00
president_apartment_price = 35.00

nights = days - 1
price = 0
discount = 1

if accommodation_type == "room for one person":

    price = room_for_one_person_price * nights

elif accommodation_type == "apartment":

    price = apartment_price * nights

    if days < 10:
        discount = 0.70
    elif 10 <= days <= 15:
        discount = 0.65
    elif days >= 15:
        discount = 0.5

elif accommodation_type == "president apartment":

    price = president_apartment_price * nights

    if days < 10:
        discount = 0.90
    elif 10 <= days <= 15:
        discount = 0.85
    elif days >= 15:
        discount = 0.8

price *= discount

if grade == "positive":
    print(f'{price * 1.25 :.2f}')

elif grade == "negative":
    print(f'{price * 0.9 :.2f}')
