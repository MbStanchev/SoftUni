cout_of_flores = int(input())
cout_of_rooms = int(input())

for i in range (cout_of_flores, 0, -1):
    for j in range (0, cout_of_rooms):
        if i == cout_of_flores:
            print(f"L{i}{j}", end=" ")
        elif i % 2 == 0:
            print(f"O{i}{j}",end=" ")
        else:
            print(f"A{i}{j}",end=" ")
    print()