import time
def myfun():
    n=0
    n1=0
    while(n1<10000):
        while(n<10000):
            n=n+1
        n1=n1+1
    return n1
        
print("Enter yor name: ")
start_time=time.time()
#name=input()
print(myfun())
elapsed =time.time() - start_time

print("it took you",elapsed,"seconds to respond")
