string = input()
printing = False
while string != "End":
    if string != "SoftUni":
        printing = True
    elif string == "SoftUni":
        printing = False
        string = input()
        continue
    print("".join([char*2 for char in string]))
    string = input()
    # for char in string:
    #
    #     if printing:
    #         print(char * 2, end= "")
    # string = input()
    # print()
    #gogoogog
