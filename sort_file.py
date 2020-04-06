with open("runs.txt",mode="r") as numfile:
    numbers=numfile.read().split("\n")
    
numbers1=[]
print(numbers)

for i in numbers:
    numbers1.append(int(i))
'''numbers1.sort()
print(numbers1)'''
sorted_number=sorted(numbers1)
print("Sorted numbers: ",sorted_number)
 
