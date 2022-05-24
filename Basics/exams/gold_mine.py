num_locations = int(input())
for i in range(num_locations):
    expected_mined = float(input())
    num_of_days = int(input())
    all_mined_gold = 0
    avarage_mined = 0

    for j in range (num_of_days):
        mined_gold = float(input())
        all_mined_gold += mined_gold

    avarage_mined = all_mined_gold / num_of_days
    diff = abs(expected_mined - avarage_mined)
    if avarage_mined >= expected_mined:
        print(f"Good job! Average gold per day: {avarage_mined:.2f}.")
    else:
        print(f"You need {diff:.2f} gold.")
