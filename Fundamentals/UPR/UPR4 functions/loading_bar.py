num = int(input())
list = []
porcent = 0
if 0 <= num <= 90 and num % 10 == 0:
    porcent = num // 10
    list.append(porcent * "%")
    list.append((10 - porcent) * ".")

    print(f"{num}%",end=" ")
    print(f"[{''.join(list)}]")
    print("Still loading...")
else:
    if num == 100:
        print("100% Complete!")
        print("[%%%%%%%%%%]")

    else:
        pass