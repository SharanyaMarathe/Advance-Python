import time
def manystring_dec(func):
    def wrapper(num):
        start=time.time()
        msg=func(num)
        msg2= [strings.upper() for strings in msg]
        end=time.time()
        print(f"Time taken :{end-start:.6f}seconds")
        return msg2
    return wrapper

@manystring_dec
def many_strings(num):
        strings=["Hello world" for i in range(num)]
        return strings


number=int(input("Enter number of strings needed in the sting list:"))
names=many_strings(number)
print(names)
#print(start,end)
#print(len(names))
#total=sum(map(len,names))
#print(total)
