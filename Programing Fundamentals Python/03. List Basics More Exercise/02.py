def is_winning_combination(n1, n2, n3):
    if n1 == n2 == n3 and n1 != 0:
        return True
    else:
        return False


def check_horizontal(board, winner):
    for i in range(0, 3):
        if is_winning_combination(board[i][0], board[i][1], board[i][2]):
            winner = board[i][0]
    return winner


def check_vertical(board, winner):
    for i in range(0, 3):
        if is_winning_combination(board[0][i], board[1][i], board[2][i]):
            winner = board[0][i]
    return winner


def check_diagonals(board, winner):
    if is_winning_combination(board[0][0], board[1][1], board[2][2]):
        return board[0][0]
    elif is_winning_combination(board[0][2], board[1][1], board[2][0]):
        return board[2][0]
    else:
        return winner


winner = 0

board = [
    [int(x) for x in input().split()],
    [int(x) for x in input().split()],
    [int(x) for x in input().split()]
]


winner = check_vertical(board, winner)
winner = check_horizontal(board, winner)
winner = check_diagonals(board, winner)

if winner == 1:
    print("First player won")
elif winner == 2:
    print("Second player won")
else:
    print("Draw!")
