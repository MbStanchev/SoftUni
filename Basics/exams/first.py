num_of_people_in_group = int(input())
num_of_nights = int(input())
num_transport_cards = int(input())
num_of_musiem_tickets = int(input())

price_per_night = 20
price_transport_card = 1.60
price_musiem_ticket = 6

cost_nights = num_of_nights * 50
cost_transport = num_transport_cards * price_transport_card
cost_musiem = price_musiem_ticket * num_of_musiem_tickets

all_cost = (cost_musiem + cost_nights + cost_transport) * 50
total = all_cost + all_cost * 0.25
print(f"{total:.2f}")