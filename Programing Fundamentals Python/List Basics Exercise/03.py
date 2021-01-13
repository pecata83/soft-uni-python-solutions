cards = input()

team_a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
team_b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

cards_list = cards.split()
game_stopped = False

for card in cards_list:
    split_card = card.split("-")
    team = split_card[0]
    player_number = int(split_card[1])

    if team == "A" and player_number in team_a:
        team_a.remove(player_number)

    if team == "B" and player_number in team_b:
        team_b.remove(player_number)

    if len(team_a) < 7 or len(team_b) < 7:
        game_stopped = True
        break

print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")

if game_stopped:
    print("Game was terminated")
