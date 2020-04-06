def Check_capacity(weights):
   total=0 
   for i in weights:
        total+=i
        if (total > 400):
            break
        
   print(total-i)
   print("Total number of people : ",weights.index(i))

        
weights=[64,80,10,110,75,35,94,70,45,65]
capacity=400

Check_capacity(weights)
sorted(weights,reverse=True)
#print(weights)
print("In any order if the people enter the lift")
Check_capacity(weights)

