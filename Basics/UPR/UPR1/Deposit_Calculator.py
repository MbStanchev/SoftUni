deposit = float(input())
months = int(input())
yearly_interest = float(input())

total_sum = deposit + months * ((deposit * yearly_interest) / 100 / 12)
#monthly_interest = (deposit * yearly_interest) / 100 / 12
#totat_sum = deposit * monthly_interest * months
print(total_sum)
#сума = депозирана сума  + срок на депозита * ((депозирана сума * годишен лихвен процент ) / 12)
