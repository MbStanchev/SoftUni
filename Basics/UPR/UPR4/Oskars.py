actors_name = input()
poits_have = float(input())
num_of_jurey = int(input())
total_points = 0
for i in range (num_of_jurey):

    name_of_jurry = input()
    points_from_jurry = float(input())

    points = len(name_of_jurry) * points_from_jurry / 2
    poits_have += points

    if poits_have > 1250.5:
        break
if poits_have > 1250.5:
    print(f"Congratulations, {actors_name} got a nominee for leading role with {poits_have:.1f}!")
else:
    diff = 1250.5 - poits_have
    print(f"Sorry, {actors_name} you need {diff:.1f} more!")