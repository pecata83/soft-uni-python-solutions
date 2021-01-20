kozunak_count = int(input())

best_baker_score = 0
best_baker_name = ""


for i in range(1, kozunak_count + 1):

    baker_name = input()
    command = input()
    baker_score = 0

    while command != "Stop":
        baker_score += int(command)
        command = input()
    else:
        print(f"{baker_name} has {baker_score} points.")
        if baker_score > best_baker_score:
            best_baker_score = baker_score
            best_baker_name = baker_name
            print(f"{best_baker_name} is the new number 1!")


print(f"{best_baker_name} won competition with {best_baker_score} points!")
