student = 0
standard = 0
kid = 0
total_counter = 0
movie_name = input()
while movie_name != "Finish":
    free_seats = int(input())
    availability = free_seats
    sold_seats = 0

    while availability > 0:
        type_of_ticket = input()
        if type_of_ticket == "End":
            break
        if type_of_ticket == "student":
            student += 1
            availability -= 1
        elif type_of_ticket == "standard":
            standard += 1
            availability -= 1
        elif type_of_ticket == "kid":
            kid += 1
            availability -= 1
        total_counter += 1
    movie_name = input()

print()
