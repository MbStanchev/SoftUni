comand = input()
max_num = 0
head_trick = False
save_name = ""
while comand != "END":
    name = comand
    num_of_goals = int(input())
    if num_of_goals > max_num:
        max_num = num_of_goals
        save_name = name
    if num_of_goals >= 3:
        head_trick = True
    if num_of_goals >= 10:
        break
    comand = input()

print(f"{save_name} is the best player!")
if head_trick:
    print(f"He has scored {max_num} goals and made a hat-trick !!!")
else:
    print(f"He has scored {max_num} goals.")