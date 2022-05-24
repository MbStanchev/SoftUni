record = float(input())
distance = float(input())
time_s_m = float(input())

time = distance * time_s_m
time_with_delay = (distance // 15) * 12.5
total_time = time + time_with_delay

difference = abs(record - total_time)

if total_time < record:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
else:
    print(f"No, he failed! He was {difference:.2f} seconds slower.")