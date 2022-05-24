destenation = input()
vecation_buget = float(input())
savings = 0
done = False
while destenation != "End":

    dayly_savings = float(input())
    savings += dayly_savings
    if savings >= vecation_buget:
        print(f"Going to {destenation}!")
        destenation = input()
        if destenation == 'End':
            break
        vecation_buget = float(input())
        savings = 0




