num_days_off = int(input())
max_play_time = 30000

work_days = 365 - num_days_off
play_time = num_days_off * 127 + work_days * 63
difference = abs(max_play_time - play_time)
hours = difference // 60
minets = difference % 60

if play_time > max_play_time:
    print("Tom will run away")
    print(f"{hours} hours and {minets} minutes more for play")

else:
    print("Tom sleeps well")
    print(f"{hours} hours and {minets} minutes less for play")