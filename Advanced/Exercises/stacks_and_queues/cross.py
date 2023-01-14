from collections import deque
green_duration = int(input())
safe_time = int(input())
command = input()
cars_deque = deque()
cars_passed = 0
crossroad = deque()
car_in = ''
letter = ''
crash = False
while command != "END" and not crash:
    timer = green_duration
    duration = green_duration + safe_time
    if command != 'green':
        cars_deque.append(command)
    else:
        while cars_deque and timer > 0:
            car_in = cars_deque.popleft()

            if len(car_in) > timer + safe_time:
                print(f"A crash happened!\n{car_in} was hit at {car_in[timer + safe_time]}.")
                break

            timer -= len(car_in)
            cars_passed += 1

    command = input()
if not crash:
    print('Everyone is safe.')
    print(f'{cars_passed} total cars passed the crossroads.')