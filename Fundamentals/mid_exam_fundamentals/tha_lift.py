waiting_people = int(input())
lift_state = list(map(int, input().split()))

for current_cabin in range(len(lift_state)):
    # if lift_state[current_cabin] == 0:
        people_in_cabin = 0
        if waiting_people > 3:
            people_in_cabin = 4 - lift_state[current_cabin]
            lift_state[current_cabin] += people_in_cabin
            waiting_people -= people_in_cabin
            if sum(lift_state) == len(lift_state) * 4 and waiting_people > 0:
                print(f"There isn't enough space! {waiting_people} people in a queue!")
                print(" ".join([str(num) for num in lift_state]))
                break
            elif sum(lift_state) == len(lift_state) * 4 and waiting_people == 0:
                print(" ".join([str(num) for num in lift_state]))
                break
        else:
            lift_state[current_cabin] += waiting_people
            print(f"The lift has empty spots!")
            print(" ".join([str(num) for num in lift_state]))
            break
    # else:
    #     diff = abs(lift_state[current_cabin] - 4)
    #     lift_state[current_cabin] += diff
    #     waiting_people -= diff