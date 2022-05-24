wight = int(input())
lenght = int(input())
all_peases = wight * lenght
left = False
while all_peases > 0:
    take = input()
    if take == "STOP":
        left = True
        break
    take = int(take)
    all_peases -= take

if left:
    print(f"{all_peases} pieces are left.")
else:
    print(f"No more cake left! You need {abs(all_peases)} pieces more.")