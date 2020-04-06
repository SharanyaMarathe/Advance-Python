def add(num1,num2):
    return num1+num2

def sub(num1,num2):
    return num1-num2

alpha=10
beta=20
total=add(alpha,beta)
print("sum: ",total)
subtarct=sub(alpha,beta)
print("Difference: ",subtarct)

Aus_runs1=250
India_runs1=220
Aus_runs2=150
Aus_total=add(Aus_runs1,Aus_runs2)
India_runs2=sub(Aus_total,India_runs1)
India_total=add(India_runs2,1)
print("India should score:  ",India_total)

veg=120
fruit=55
cash=200
total=add(veg,fruit)
retuns=sub(cash,total)
print("Cashier will return rupees: ",retuns)
