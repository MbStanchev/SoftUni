hour = int(input())
minute = int(input())
will_be_min = (minute + 15) % 60
will_be_hour = ((minute + 15) // 60) + hour
if will_be_hour > 23:
    will_be_hour = 0
print(f"{will_be_hour}:{will_be_min:02d}")
#print(will_be_hour)