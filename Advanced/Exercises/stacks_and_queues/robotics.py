from collections import deque


def orig_time(sec):
    sec %= 24 * 60 * 60
    h = sec // 3600
    m = sec % 3600 // 60
    s = sec % 3600 % 60
    return f'[{h:02d}:{m:02d}:{s:02d}]'


input_list_enry_data_robots = list(input().split(';'))
start_time = list((int(x) for x in input().split(':')))
itm = input()


robots_prosess_time = {}
robots_working_till = {}
list_of_detalis = deque()
h, m, s = start_time
time_in_sec = s + m*60 + h*60*60


while itm != 'End':
    list_of_detalis.append(itm)
    itm = input()

for pair in input_list_enry_data_robots:
    robo, proces = pair.split('-')
    robots_prosess_time[robo] = int(proces)
    robots_working_till[robo] = -1

while list_of_detalis:
    time_in_sec += 1
    current_itm = list_of_detalis.popleft()
    for name, buisy_until in robots_working_till.items():
        if buisy_until <= time_in_sec:
            robots_working_till[name] = time_in_sec + robots_prosess_time[name]
            print(f'{name} - {current_itm} {orig_time(time_in_sec)}')
            break
    else:
        list_of_detalis.append(current_itm)