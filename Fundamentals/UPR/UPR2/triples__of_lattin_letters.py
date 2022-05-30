n = int(input())
for i in range(97, 97 + n):
    for g in range(97, 97 + n):
        for h in range(97, 97 + n):
            print(f"{chr(i)}{chr(g)}{chr(h)}")
