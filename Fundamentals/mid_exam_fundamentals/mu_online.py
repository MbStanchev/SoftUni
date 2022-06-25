health = 100
bitcoin = 0
dungeons_rooms = input().split('|')
count = 0
alive = True
for part in range(len(dungeons_rooms)):
    second_split = dungeons_rooms[part].split ()
    word = second_split[0]
    points = int(second_split[1])
    count += 1

    if word == 'potion':
        if health + points >= 100:
            points = 100 - health
            health = 100
        else:
            health += points
        print(f"You healed for {points} hp.")
        print(f"Current health: {health} hp.")

    elif word == 'chest':
        bitcoin += points
        print(f"You found {points} bitcoins.")

    else:
        health -= points
        if health > 0:
            print(f"You slayed {word}.")
        else:
            print(f"You died! Killed by {word}.")
            print(f'Best room: {count}')
            alive = False
            break
if alive:
    print("You've made it!")
    print(f"Bitcoins: {bitcoin}")
    print(f"Health: {health}")
