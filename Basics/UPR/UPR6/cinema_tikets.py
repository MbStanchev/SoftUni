name_of_movie = input()
student = 0
standart = 0
kid = 0
total_couter = 0
while name_of_movie != "Finish":
    seats_in_theatre = int(input())
    sold_seats = 0
    sold = 0
    curent_counter = 1
    capasiaty = 0
    while curent_counter <= seats_in_theatre:
        type_of_ticket = input()
        if type_of_ticket == "End":
            break
        elif type_of_ticket == "student":
            student += 1
        elif type_of_ticket == "standard":
            standart += 1
        elif type_of_ticket == "kid":
            kid += 1
        curent_counter += 1
        total_couter += 1
        sold += 1
    sold_seats += student + standart + kid
    capasiaty = sold / seats_in_theatre * 100
    print(f"{name_of_movie} - {capasiaty:.2f}% full.")
    name_of_movie = input()
student_procent = student / total_couter * 100
standart_procent = standart / total_couter * 100
kid_procent = kid / total_couter * 100

print(f"Total tickets: {total_couter}")
print(f"{student_procent:.2f}% student tickets.")
print(f"{standart_procent:.2f}% standard tickets.")
print(f"{kid_procent:.2f}% kids tickets.")
