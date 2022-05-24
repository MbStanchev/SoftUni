food = int(input())
all_foof = 0
adopted = False
while food >= 0:
    grams = str(input())
    if grams != "Adopted":
        intgrams = int(grams)
        all_foof += intgrams
        adopted = True
    else:
        break
diff = abs((food * 1000) - all_foof)


if all_foof <= (food * 1000):
    print(f"Food is enough! Leftovers: {diff} grams.")
else:
    print(f"Food is not enough. You need {diff} grams more.")