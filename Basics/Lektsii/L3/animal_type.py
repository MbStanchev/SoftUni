type_animal = input()

#2.	crocodile, tortoise, snake -> reptile

is_mammal = type_animal == "dog"
is_reptile = type_animal == "crocodile" or type_animal == "tortoise" or type_animal == "snake"

if is_mammal:
    print("mammal")
elif is_reptile:
    print("reptile")
else:
    print("unknown")