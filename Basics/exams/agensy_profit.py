name_of_airline = input()
num_adult_tickets = int(input())
num_kids_tickets = int(input())
price_of_adult_tickets = float(input())
price_tax = float(input())

price_of_kids_tickets = price_of_adult_tickets * 0.3
price_adult_whit_tax = price_of_adult_tickets + price_tax
price_kids_whit_tax = price_of_kids_tickets + price_tax

total = (num_adult_tickets * price_adult_whit_tax) + (num_kids_tickets * price_kids_whit_tax)
profit = total * 0.2
print(f"The profit of your agency from {name_of_airline} tickets is {profit:.2f} lv.")