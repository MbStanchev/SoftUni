import random
print("Let's play the game - Guess the number from 1 to 100\nYou have 10 tries")

list1 = list(range(1,101))
counter_of_sugestions = 0
suggestions = []
current_num = random.choice(list1)
for i in range(10):

    sugestion = input("Enter your sugestion: ")

    current_num = int(current_num)
    sugestion = int(sugestion)

    if sugestion in suggestions:
        print("You'v tride that one!!\n")
        continue
    suggestions.append(sugestion)

    if sugestion != current_num:
        print("Wrong")

        if sugestion < current_num:
            print("the num is higher!\n")
            counter_of_sugestions +=1
        elif sugestion > current_num:
            print("The num is lower!\n")
            counter_of_sugestions += 1
    else:
        print(f"congratilations you guest the number {current_num}")
        print(f"you guest the num in {counter_of_sugestions} tries")
        break

else:
    print(f"Good luck next time \nThe number is {current_num}")




