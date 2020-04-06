class Date:
     def __init__(self,dd,mm,yy):
         self.d=dd
         self.m=mm
         self.y=yy

     def display(self):
         dt=self.d
         mn=self.m
         yr=self.y
         print(f"Display {dt}-{mn}-{yr}")

     def __str__(self):
          dt=self.d
          mn=self.m
          yr=self.y
          return f"Str {dt}/{mn}/{yr}"

     def __repr__(self):
          dt,mn,yr=self.d,self.m,self.y
          return f"Date {dt}/{mn}/{yr}"
            


today=Date(9,3,2020)
today.display()
print(today) # calls __str__
print(repr(today))# calls __repr__
             
