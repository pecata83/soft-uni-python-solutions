sums = input().split(", ")
begars = int(input())

begars_earnings = []

for beggar in range(0, begars):
    earning = 0
    for s in range(beggar, len(sums), begars):
        earning += int(sums[s])

    begars_earnings += [earning]

print(begars_earnings)