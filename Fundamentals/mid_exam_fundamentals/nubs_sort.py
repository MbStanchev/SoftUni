# moving_targets
def shoot_func(index, power, targets):
    if 0 <= index < len(targets):
        if targets[index] - power <= 0:
            targets.pop(index)
        else:
            targets[index] -= power

    return targets


def add_func(index, value, targets):
    if 0 <= index < len(targets):
        targets.insert(index, value)
    else:
        print("Invalid placement!")

    return targets


def strike_func(index, radius, targets):
    validator_index = index - radius >= 0 and index + radius < len(targets)

    if validator_index:
        start_target_index = index - radius
        final_target_index = index + radius
        targets = [targets[i] for i in range(len(targets)) if i < start_target_index or i > final_target_index]
    else:
        print("Strike missed!")

    return targets


def moving_targets(targets):
    while True:
        command = input()

        if command == 'End':
            print('|'.join([str(num) for num in targets]))
            break

        command = command.split(' ')
        current_command = command[0]
        first_element = int(command[1])
        second_element = int(command[2])

        if current_command == 'Shoot':
            targets = shoot_func(first_element, second_element, targets)
        elif current_command == 'Add':
            targets = add_func(first_element, second_element, targets)
        elif current_command == 'Strike':
            targets = strike_func(first_element, second_element, targets)


data = list(map(int, input().split(' ')))
moving_targets(data)


# The Lift
def lift_func(waiting_people, current_state_of_the_lift):
    for i in range(len(current_state_of_the_lift)):
        if waiting_people > 3:
            current_number_of_people = abs(4 - int(current_state_of_the_lift[i]))
            waiting_people -= current_number_of_people
            current_state_of_the_lift[i] += current_number_of_people
        else:
            current_state_of_the_lift[i] += waiting_people
            waiting_people = 0

    if waiting_people > 0:
        print(f"There isn't enough space! {waiting_people} people in a queue!")
    elif sum(current_state_of_the_lift) != len(current_state_of_the_lift) * 4:
        print(f"The lift has empty spots!")

    print(' '.join([str(num) for num in current_state_of_the_lift]))


number_of_people = int(input())
lift_condition = list(map(int, input().split(' ')))
lift_func(number_of_people, lift_condition)

# counter_strike
energy = int(input())
won_battle_counter = 0

while True:
    command = input()

    if command == 'End of battle':
        print(f'Won battles: {won_battle_counter}. Energy left: {energy}')
        break

    distance = int(command)

    if energy >= distance:
        energy -= distance
        won_battle_counter += 1

        if won_battle_counter % 3 == 0:
            energy += won_battle_counter

    else:
        print(f'Not enough energy! Game ends with {won_battle_counter} won battles and {energy} energy')
        break