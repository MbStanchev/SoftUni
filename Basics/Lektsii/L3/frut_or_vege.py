name = input()

#"fruit" имат следните възможни стойности:  banana, apple, kiwi, cherry, lemon и grapes;
#"vegetable" имат следните възможни стойности:  tomato, cucumber, pepper и carrot;

is_fruit = name == "banana" or name == "apple" or name == "kiwi" or name == "cherry" or name == "lemon" or name == "grapes"
is_vegy = name == "tomato" or name == "cucumber" or name == "pepper" or name == "carrot"

if is_fruit:
    print("fruit")
elif is_vegy:
    print("vegetable")
else:
    print("unknown")