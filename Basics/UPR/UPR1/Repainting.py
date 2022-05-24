

nailon = int(input())
paint = int(input())
thinner = int(input())
working_hours = int(input())
price_of_nailon = 1.5
price_of_paint = 14.50
price_of_thinner = 5
plastic_bag = 0.40
price_of_materials = (nailon + 2) * price_of_nailon + \
                     (paint * 1.1) * price_of_paint + \
                     thinner * price_of_thinner + \
                     plastic_bag
price_for_work_hour = price_of_materials * 0.3
total_price = price_of_materials + price_for_work_hour * working_hours
print(total_price)