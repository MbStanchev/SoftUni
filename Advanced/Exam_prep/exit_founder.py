names = input().split(", ")
n = 6
matrix = []
to_rest = {}
for _ in range(n):
    matrix.append(input().split())

while True:
    command = [int(x) for x in input().strip("()").split(", ")]
    pos = matrix[command[0]][command[1]]
    if names[0] in to_rest.keys() and to_rest[names[0]] > 0:
        to_rest[names[0]] -= 1
        names[0], names[1] = names[1], names[0]
        continue
    if pos == "E":
        print(f"{names[0]} found the Exit and wins the game!")
        break
    elif pos == "T":
        print(f"{names[0]} is out of the game! The winner is {names[1]}.")
        break
    elif pos == "W":
        print(f"{names[0]} hits a wall and needs to rest.")
        if names[0] not in to_rest.keys():
            to_rest[names[0]] = 0
        to_rest[names[0]] += 1

    names[0], names[1] = names[1], names[0]
