lenght = int(input())
width = int(input())
hight = int(input())
percent_volume = float(input())

area = lenght * width * hight
area_in_dsm = area * 0.001
watter_area = area_in_dsm - (area_in_dsm * percent_volume / 100)
print(watter_area)

