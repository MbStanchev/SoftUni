from collections import deque
available_watter = int(input())
people = input()
line = deque()
while people != 'Start':
    line.append(people)
    people = input()
command = input()
while command != 'End':
    if 'refill' in command:
        command, litters_to_reffil = command.split()
        available_watter += int(litters_to_reffil)
    elif command.isdigit():
        required_litters = int(command)
        if available_watter >= required_litters:
            available_watter -= required_litters
            print(f'{line.popleft()} got water')
        else:
            print(f'{line.popleft()} must wait')
    command = input()
print(f'{available_watter} liters left')