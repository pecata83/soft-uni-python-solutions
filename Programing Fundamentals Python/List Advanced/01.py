wagons = int(input())

train = [0 for w in range(wagons)]

while True:
    command_input = input().split()
    command = command_input[0]
    index = int(command_input[1]) if len(command_input) > 1 else None
    people = int(command_input[2]) if len(command_input) > 2 else None

    if command == "End":
        break
    elif command == "add":
        train[-1] += index
    elif command == "insert":
        train[index] += people
    elif command == "leave":
        train[index] -= people

print(train)
