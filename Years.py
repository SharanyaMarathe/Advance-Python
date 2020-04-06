distance=10000
print("Sandeep rides 5 hours per day")
speed=int(input("Enter speed in Km/h"))
if speed<=0:
    print("Sandeep didn't ride")
    
else:
    days=distance/(speed*5)
    print("Total Days: ",days)
    years=days//365
    print("Years: ",years)
    years1=days%365
    months=years1//30
    print("Months: ",months)
    months1=years1%30
    print("Days: ",months1)
    hrs=(months1*24)%24
    hrs1=months1%24
    print("Hrs: ",hrs)
    mins=hrs1*60//60
    print("Minutes: ",mins)
    sec=hrs1%60
    print("Seconds: ",sec)
