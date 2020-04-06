def first_five():
      c=1
      for line in file1:
           captains_name=line.split(",")
           print(str(c)+"captain: ",captains_name[0]+"  "+captains_name[1])
           c=c+1
           if(c>5):
             break
def capt_2000():
      
      c=1 
      c_year1=[]
      for line in file1:
           if int(line.split(",")[1].split("-")[0]) >= 2000:
            print("{} ---> {}".format(line.split(",")[0],line.split(",")[1]))
           else:
             continue
                  
def name_match():
      li=list()
      for line in file1:
           li.append(line)   
      li.sort()
      for item in li:
           print("{} ---> {}".format(item.split(",")[0],item.split(",")[2]))

def math_name():
      n_matches=list()
      for line in file1:
            captains_name=line.split(",")
            n_matches.insert(0,int(captains_name[2]))
            n_matches.insert(1,captains_name[0])

      n_matches.sort()      
      for item in n_matches:
            print("{}---------->{}".format(item.split(",")[2],item.split(",")[0]))

while(True):     
      print("1.Print 1st 5 captains\n2.Print captians name who played since 2000\n3.Sort based on captain's nameand print number of mathes")
      print("4.Print name based on number of mathes played\n5.Exit")
      ch=int(input("Enter choice: "))
      
      if(ch==1):
            
            print("First five captains")
            with open("captains.txt",mode="r") as file1:
                  header=next(file1)
                  first_five()
            print("==========================")
      if(ch==2):
            print("Captains since 2000")
            with open("captains.txt",mode="r") as file1:
                  header=next(file1)
                  capt_2000()
            print("==========================")
      if(ch==3):
            print("Name and Number of matches")
            with open("captains.txt",mode="r") as file1:
                  header=next(file1)
                  name_match()
            print("==========================")
            
      if(ch==4):
            print("Name and Number of matches")
            with open("captains.txt",mode="r") as file1:
                  header=next(file1)
                  math_name()
            print("==========================")
      if(ch==5):
            print("Thanks")
            break
