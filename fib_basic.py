def fib_gen():
    a=1
    b=1
    flag=0
    fib_list=list()
    print("===================")
    while(flag<10):
        yield b
        a,b=b,a+b
        flag+=1

if(__name__=="__main__"):       
    all_nums=fib_gen()
    for num in all_nums:
        print(num **2)
