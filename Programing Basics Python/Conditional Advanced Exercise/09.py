import math

year_type = input()
bank_holidays = int(input())
weekends_home = int(input())

games_in_sofia = (48 - weekends_home) / 4 * 3
bank_holidays_games = bank_holidays / 3 * 2

total_games = weekends_home + games_in_sofia + bank_holidays_games

if year_type == "normal":
    print(math.floor(total_games))
elif year_type == "leap":
    total_games *= 1.15
    print(math.floor(total_games))
