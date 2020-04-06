with open ("Book1.csv",mode="r") as file1:
    
    scores=list()
    #print(file1.read())
    for line in file1:
        scs=list(map(int,(line.split(","))))
        #print(scs)
        for item in scs:
            scores.append(scs)

#print(scores)
            
for lines in scores:
    
          if(lines[0]-lines[1]+lines[2]==lines[3]-1):
               print("Data Matches")
          else:
               print("Data Not matches,Please correct the data")
          
'''num=0         
i=iter(scores)
while(num<12):
    if(next(i)-next(i)+next(i)==(next(i)-1)):
         print("Data Matches")
    else:
         print("Data Not matches,Please correct the data")   
    num+=1'''
