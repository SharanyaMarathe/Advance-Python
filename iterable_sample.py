class Container():
    def __init__(self,n):
        self.val=0
        self.maxval=n
        
    def __iter__(self):
            return self
        
    def __next__(self):
       if self.val< self.maxval:
           retval=self.val
           self.val+=1
           return retval
       else:
           raise StopIteration()
  
    
bag=Container(5)
for item in bag:
    print(item)
