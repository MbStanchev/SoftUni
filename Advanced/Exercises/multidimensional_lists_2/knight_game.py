n = int(input())


chest_board = [list(input()) for _ in range(n)]

moves_of_knight = (
    (2, 1),
    (2, -1),
    (1, -2),
    (-1, -2),
    (-2, -1),
    (-2, 1),
    (-1, 2),
    (1, 2)
)


removed = 0
while True:
    attacks = 0
    attacker_pos = []
    for row in range(n):
        for col in range(n):
            current_attacks = 0
            current_attacker_pos = []
            if chest_board[row][col] == 0:
                continue
            if chest_board[row][col] == 'K':
                for moves in moves_of_knight:
                    r = row + moves[0]
                    c = col + moves[1]
                    if not (0 <= r < len(chest_board) and 0 <= c < len(chest_board)):
                        continue
                    if chest_board[r][c] == 0:
                        continue
                    elif chest_board[r][c] == 'K':
                        current_attacks += 1

                if current_attacks > attacks:
                    attacks = current_attacks
                    attacker_pos = row, col

    if attacks:
        chest_board[attacker_pos[0]][attacker_pos[1]] = 0
        removed += 1
    else:
        break
print(removed)
