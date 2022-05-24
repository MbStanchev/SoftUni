import math
area = 0
figure = input()
if figure == "square":
    a = float(input())
    area = a * a
elif figure == "rectangle":
    a = float(input())
    b = float(input())
    area = a * b
elif figure == "circle":
    a = float(input())
    area = math.pi * a * a
elif figure == "triangle":
    a = float(input())
    b = float(input())
    area = a*b/2
print(f"{area:.2f}")
#print(f'{n=:.2f}')
