w = int(input())
l = int(input())
h = int(input())
finish = False
free_space = w * l * h

while free_space >= 0:

    num_of_box = input()
    if num_of_box == "Done":
        finish = True
        break
    num_of_box = int(num_of_box)
    free_space -= num_of_box

if finish:
    print(f"{free_space} Cubic meters left.")
else:
    print(f"No more free space! You need {abs(free_space)} Cubic meters more.")