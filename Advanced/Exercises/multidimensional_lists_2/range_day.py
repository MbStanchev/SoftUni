n = 5
matrix = []
yes = False
all_targets = 0
hit_targets = 0
hit_pos = []
shooter_pos = ()
directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}
for r in range(n):
    matrix.append(input().split())
    for c in range(n):
        if matrix[r][c] == 'A':
            shooter_pos = (r, c)
        elif matrix[r][c] == 'x':
            all_targets += 1

number_of_commands = int(input())
for command in range(number_of_commands):
    if yes:
        break
    action = input().split()
    if action[0] == 'move':
        direction = action[1]
        steps = int(action[2])
        next_pos_row = (shooter_pos[0] + (directions[direction][0] * steps))
        next_pos_col = (shooter_pos[1] + (directions[direction][1] * steps))
        if not (0 <= next_pos_row < len(matrix) and 0 <= next_pos_col < len(matrix)):
            continue
        if matrix[next_pos_row][next_pos_col] == 'x':
            continue
        shooter_pos = (next_pos_row, next_pos_col)
    elif action[0] == 'shoot':
        shoot_direction = action[1]
        shooting_row = shooter_pos[0] + directions[shoot_direction][0]
        shooting_col = shooter_pos[1] + directions[shoot_direction][1]
        while 0 <= shooting_row < len(matrix) and 0 <= shooting_col < len(matrix):

            if not matrix[shooting_row][shooting_col] == 'x':
                shooting_row += directions[shoot_direction][0]
                shooting_col += directions[shoot_direction][1]
                continue
            hit_targets += 1
            hit_pos.append([shooting_row, shooting_col])
            matrix[shooting_row][shooting_col] = '.'
            break
        if hit_targets == all_targets:
            yes = True
            break

if all_targets != hit_targets:
    print(f"Training not completed! {all_targets - hit_targets} targets left.")
    print(*hit_pos, sep='\n')
else:
    print(f'Training completed! All {hit_targets} targets hit.')
    print(*hit_pos, sep='\n')
