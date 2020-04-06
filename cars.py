class Car:
    def __init__(self,start,end,fuel):
        self._end=end
        self._start=start
        self.fuel=fuel
        self.base_clr="Red"

    def get_mileage(self):
            return (self.end-self.start)/ self.fuel
        

    @property    
    def color(self):
        return self.base_clr

    @property
    def start(self):
        return self._start

    @property
    def end(self):
        return self._end

    
    '''@start.setter
    def start(self,new_val):
        if new_val > self.end:
            raise ValueError(f"{new_val} is beyond end")
        self._start = new_val''' #to avoid recursion(whenever self.start is setting to some value it calss start.setter

    @end.setter
    def end(self,new_val):
        print("Setting end to: ",new_val)
        if new_val < self.end:
            raise ValueError(f"Cannot reduce end value below {self.end}")
        self._end=new_val
        
              
     
