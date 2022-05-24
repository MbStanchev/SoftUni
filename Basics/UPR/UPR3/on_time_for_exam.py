hour = int(input())
minute = int(input())
hour_of_arrival = int(input())
minute_of_arrival = int(input())

time_of_exam = (hour * 60) + minute
time_of_arrival = (hour_of_arrival * 60) + minute_of_arrival


if time_of_exam < time_of_arrival:
    print("Late")

elif time_of_exam >= time_of_arrival >= time_of_exam - 30:
    print("On time")

elif time_of_arrival < time_of_exam - 30:
    print("Early")

difference = abs(time_of_exam - time_of_arrival)
hh = difference // 60
mm = difference % 60
if time_of_exam - 60 < time_of_arrival < time_of_exam:
    print(f"{mm} minutes before the start")

elif time_of_exam - 60 >= time_of_arrival:

    print(f"{hh}:{mm:02d} hours before the start")

elif time_of_exam < time_of_arrival < time_of_exam + 60:
    print(f"{mm} minutes after the start")

elif time_of_exam + 60 <= time_of_arrival:
    print(f"{hh}:{mm:02d} hours after the start")