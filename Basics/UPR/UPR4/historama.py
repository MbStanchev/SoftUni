n = int(input())

p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0
for i in range (n):
    current_num = int(input())
    if current_num < 200:
        p1 +=1
    elif current_num < 400:
        p2 += 1
    elif current_num < 600:
        p3 += 1
    elif current_num < 800:
        p4 += 1
    elif current_num >= 800:
        p5 += 1
p_1 = p1 / n * 100
p_2 = p2 / n * 100
p_3 = p3 / n * 100
p_4 = p4 / n * 100
p_5 = p5 / n * 100

print(f"{p_1:.2f}%")
print(f"{p_2:.2f}%")
print(f"{p_3:.2f}%")
print(f"{p_4:.2f}%")
print(f"{p_5:.2f}%")