vegtables_price = float(input())
friuts_price = float(input())
kg_vege = int(input())
kg_friuts = int(input())
sall_1 = vegtables_price * kg_vege
sall_2 = friuts_price * kg_friuts
all_sell = vegtables_price * kg_vege + \
           friuts_price * kg_friuts
euro = 1.94
all_sell_eur = all_sell / euro
print(f"{all_sell_eur:.2f}")
#print(all_sell)
#print(sall_2)
#print(sall_1)
