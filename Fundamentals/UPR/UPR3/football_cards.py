string = input()
list = string.split()
team_a = ["A-1","A-2","A-3","A-4","A-5","A-6","A-7","A-8","A-9","A-10","A-11"]
team_b = ["B-1","B-2","B-3","B-4","B-5","B-6","B-7","B-8","B-9","B-10","B-11"]
players_count_a = 0
players_count_b = 0
ok = True
for i in list:

    if i in team_a:
        team_a.remove(i)
    elif i in team_b:
        team_b.remove(i)
    players_count_a = len(team_a)
    players_count_b = len(team_b)
    if players_count_a < 7 or players_count_b < 7:
        ok = False
        break

print(f"Team A - {players_count_a}; Team B - {players_count_b}")
if not ok:
    print("Game was terminated")