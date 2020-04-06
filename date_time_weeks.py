import datetime
date=input("Input date in dd/mm/yy format")
date_l=date.split("/")
d1=datetime.date(int(date_l[2]),int(date_l[1]),int(date_l[0]))
print("Day on this date is--->",d1.strftime("%A"))
d=datetime.date(int(date_l[2]),int(date_l[1]),1)
print("First day of the week is--->",d.strftime("%A"))
month_days={1:["jan",31],2:["Feb",28],3:["Mar",31],4:["Apr",30],5:["May",31],6:["June",30],7:["July",31]
            ,8:["Aug",31],9:["Sept",30],10:["Oct",31],11:["Nov",30],12:["Dec",31]}
if((int(date_l[2])%4==0) or (int(date_l[2])%100==0) or (int(date_l[2])%400==0) or int(date_l[1])==2):
    print("This is a leap year and this month has 29 days")
else:
    print("This month is ",d1.strftime("%B"),"It has",month_days[int(date_l[1])][1],"days")
