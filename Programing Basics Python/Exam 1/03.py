prices = {
    "Argentina": {
        "flags": 3.25,
        "caps": 7.2,
        "posters": 5.1,
        "stickers": 1.25
    },
    "Brazil": {
        "flags": 4.2,
        "caps": 8.5,
        "posters": 5.35,
        "stickers": 1.2
    },
    "Croatia": {
        "flags": 2.75,
        "caps": 6.9,
        "posters": 4.95,
        "stickers": 1.1
    },
    "Denmark": {
        "flags": 3.1,
        "caps": 6.5,
        "posters": 4.8,
        "stickers": 0.9
    }
}

country_team = input()
souvenir_type = input()
souvenirs_count = int(input())

if country_team in prices:
    if souvenir_type in prices[country_team]:
        print(
            f"Pepi bought {souvenirs_count} {souvenir_type} of {country_team} for {prices[country_team][souvenir_type] * souvenirs_count:.2f} lv.")
    else:
        print("Invalid stock!")

else:
    print("Invalid country!")
