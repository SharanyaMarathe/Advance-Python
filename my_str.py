import time

def my_str(msg):
  start=time.time()
  c=0
  for i in msg:
         c+=1
  length=c
  end=time.time()
  print(f"Time taken :{end-start:.6f}seconds")
  return length


string=input("Enter a string to calculate the lenght: ")
len1=my_str(string)
print(len1)
