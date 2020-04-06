def get_operator(sym):
    def sub(num1,num2):
        return num1-num2

    def add(num1,num2):
       res=num1+num2
       return res
    
    operations={"+": add,
                "-": sub }
    op_func=operations[sym]
    return op_func

def do_work(func,one,two):
      answer=func(one,two)
      return answer

#Sum=add
#answer=add(10,20)
#answer=Sum(20,10)
#ans=do_work(add,10,30)
add_func=get_operator('+')
ans=do_work(add_func,10,20)
print(ans)
