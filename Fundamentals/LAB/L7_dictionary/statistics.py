dict = {}
count_all_products = 0
sum_all_quantities = 0
while True:
    entry = input ().split (': ')
    if entry[0] == 'statistics':
        break
    if entry[0] not in dict:
        dict[entry[0]] = 0
        count_all_products += 1
    dict[entry[0]] += int(entry[1])

    sum_all_quantities += int(entry[1])

print('Products in stock:')
for product, quantity in dict.items():

    print(f'- {product}: {quantity}')

print(f'Total Products: {count_all_products}')
print(f'Total Quantity: {sum_all_quantities}')