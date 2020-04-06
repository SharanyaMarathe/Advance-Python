class Fib_Container():
    def __init__(self,start,end):
        self.first=start
        self.last=end
        self.prev=1
        self.flag=0
        
    def __iter__(self):
            return self
        
    def __next__(self):
        if self.flag==0:
            print(self.first)
            self.flag+=1
        if  self.flag==1:
            print(self.first)
            self.flag+=1
        if self.prev<self.last:
            self.first,self.prev=self.prev,self.first+self.prev
            return self.prev
        else:
           raise StopIteration()
  
    
bag=Fib_Container(1,10)
for item in bag:
    print(item)
