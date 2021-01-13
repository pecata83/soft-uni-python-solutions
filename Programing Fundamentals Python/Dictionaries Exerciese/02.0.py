from collections import defaultdict

resources = defaultdict(int)

while True:
    command = input()

    if command == "stop":
        break

    value = int(input())

    resources[command] += value

for k, v in resources.items():
    print(k, "->", v)
