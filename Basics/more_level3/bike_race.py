num_juniors = int(input())
num_seniors = int(input())
all = num_seniors + num_juniors
track = input()
raced_money = 0
after_expences = 0
if track == "trail":
    raced_money = (num_seniors * 7) + (num_juniors * 5.5)
elif track == "cross-country":
    raced_money = (num_seniors * 9.5) + (num_juniors * 8)
    if all >= 50:
        raced_money = raced_money * 0.75
elif track == "downhill":
    raced_money = (num_seniors * 13.75) + (num_juniors * 12.25)
elif track == "road":
    raced_money = (num_seniors * 21.5) + (num_juniors * 20)

after_expences = raced_money * 0.95
print(f"{after_expences:.2f}")
