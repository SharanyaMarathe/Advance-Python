def match_name():
      li=list()
      lastname=list()
      for line in file1:
             if len(line.split()) > 2:
               li.append(line.split()[2])
             else:
               li.append(line.split()[1])  
      li.sort()
      for item in li:
         print("{}---------->{}".format(item.split(",")[0],item.split(",")[2]))

print("Name and Number of matches")
with open("captains.txt",mode="r") as file1:
         header=next(file1)
         match_name()
print("==========================")
