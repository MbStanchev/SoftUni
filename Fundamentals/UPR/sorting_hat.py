name = input()
bad_word = False
while name != "Welcome!":
    if name == "Voldemort":
        print("You must not speak of that name!")
        bad_word = True
        break
    if len(name) < 5:
        print(f"{name} goes to Gryffindor.")
    elif len(name) == 5:
        print(f"{name} goes to Slytherin.")
    elif len(name) == 6:
        print(f"{name} goes to Ravenclaw.")
    elif len(name) > 6:
        print(f"{name} goes to Hufflepuff.")
    name = input()
if not bad_word:
    print("Welcome to Hogwarts.")