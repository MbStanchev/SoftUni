movie = input()
num_roles = int(input())
num_colums = int(input())
ticket_price = 0

total_seats = num_colums * num_roles

if movie == "Premiere":
    ticket_price = 12

elif movie == "Normal":
    ticket_price = 7.5

else:
    ticket_price = 5
income = ticket_price * total_seats
print(f"{income:.2f} leva")