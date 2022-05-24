vecation_money = float(input())
have_money = float(input())
spender = False
spend_counter = 0
curent_money = 0
couner = 0
while vecation_money > have_money:
    save_spend = input()
    amount_save_spend = float(input())
    couner += 1
    if save_spend == "save":
        have_money += amount_save_spend
        spend_counter = 0
    elif save_spend == "spend":
        spend_counter += 1
        have_money -= amount_save_spend
        if have_money < 0:
            have_money = 0
        if spend_counter == 5:
            spender = True
            break
if spender:
    print("You can't save the money.")
    print(f"{couner}")
else:
    print(f"You saved the money for {couner} days.")