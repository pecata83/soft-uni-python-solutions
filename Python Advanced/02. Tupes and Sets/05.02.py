from collections import deque

players = deque(input().split())
remove_interval = int(input())

toss = 0

while len(players) > 1:
    player = players.popleft()
    toss += 1

    if toss % remove_interval == 0:
        print(f"Removed {player}")
        toss = 0
    else:
        players.append(player)


print(f"Last is {players.popleft()}")
