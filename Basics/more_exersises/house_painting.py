x = float(input())
y = float(input())
h = float(input())
window = 1.5 * 1.5
door = 2 * 1.2
side_1_green = x * x + ((x * x) - door)
side_2_green = 2 * ((x * y)- window)

roof_side_1 = 2 * (x * y)
roof_side_2  = 2 * (x * h /2)


all_green = side_1_green + side_2_green
all_roof = roof_side_2 + roof_side_1

total_green_paint = all_green / 3.4
total_red_paint = all_roof / 4.3
print(f"{total_green_paint:.2f}")
print(f"{total_red_paint:.2f}")
