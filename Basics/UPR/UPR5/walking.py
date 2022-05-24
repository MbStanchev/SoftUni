goal = 10000
done = False
steps_walked = input()
sum_of_dayly_steps = 0

while steps_walked != "Going home":

    steps_walked = int(steps_walked)
    sum_of_dayly_steps += steps_walked
    if sum_of_dayly_steps >= goal:
        done = True
        break
    steps_walked = input()
if steps_walked == "Going home":
    steps_walked = int(input())
    sum_of_dayly_steps += steps_walked
if sum_of_dayly_steps >= goal:
    done = True
diff = abs(goal - sum_of_dayly_steps)
if done:
    print("Goal reached! Good job!")
    print(f"{diff} steps over the goal!")
else:
    print(f"{diff} more steps to reach goal.")


