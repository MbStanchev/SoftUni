
#	Пакет химикали - 5.80 лв.
#	Пакет маркери - 7.20 лв.
#	Препарат - 1.20 лв (за литър)
box_of_pens = int(input())
box_of_marcers = int(input())
box_of_deturgen = int(input())
prosent_discount = float(input())
price_of_pen = 5.8
price_of_marcers = 7.2
price_of_deturgen =  1.2

total_price = box_of_pens  * price_of_pen + \
              box_of_marcers * price_of_marcers + \
              box_of_deturgen * price_of_deturgen
total_price = total_price - total_price * prosent_discount / 100
print(total_price)
