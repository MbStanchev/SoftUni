start_energy = int(input())

won_battle = 0
comand = input()
while comand != "End of battle":
    distance = int(comand)

    if distance <= start_energy:
        won_battle += 1
        start_energy -= distance
    else:
        print(f"Not enough energy! Game ends with {won_battle} won battles and {start_energy} energy")
        break
    if won_battle % 3 ==0:
        start_energy += won_battle
    comand = input()
if comand == "End of battle":
    print(f"Won battles: {won_battle}. Energy left: {start_energy}" )
