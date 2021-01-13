electrons = int(input())

current_shell = 1
shells = []

while True:
    shell_limit = 2 * current_shell ** 2
    current_shell += 1

    if electrons >= shell_limit:
        electrons -= shell_limit
        shells.append(shell_limit)
    elif electrons == 0:
        break
    elif electrons < shell_limit:
        shells.append(electrons)
        break

print(shells)
