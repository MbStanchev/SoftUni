#The final price is: {крайна цена на услугата} lv.
#The discount is: {отстъпка} lv.

squer_meters = float(input())
total_price = squer_meters * 7.61
discout = total_price * 0.18
final_price_disc = total_price - discout
print(f'The final price is: {final_price_disc} lv.')
print(f'The discount is: {discout} lv.')
