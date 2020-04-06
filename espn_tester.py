with open ("Book1.csv",mode="r") as file1:
    i=0
    scores=list()
    #print(file1.read())
    for line in file1:
        scs=list(line.split(","))
        print(scs)
        for item in scs:
          scores.append(int(item))
for item in scores:
    print(item(0))
    print("TT")
    
