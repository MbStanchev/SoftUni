comand = input()
days = 1
goal = 8848
first_step = 5364
done = False
while comand != "END":

    if comand == "Yes":
        days += 1
    elif comand == "No":
        pass
    if days > 5:
        break
    climed = int(input())
    first_step += climed
    if first_step >= goal:
        done = True
        break
    comand = input()
if done:
    print(f"Goal reached for {days} days!")
else:
    print("Failed!")
    print(f"{first_step}")
