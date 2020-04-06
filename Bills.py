class Bill:
    def __init__(self,items):
        self.vals=items[:]

    def total(self):
            return sum(self.vals)
        
    def cashback(self):
            #return 0.1*self.__total()
            return 0.1*self._total()
            #return 0.1*self.total()
        
    _total= total
    #__total=total

class GSTBill(Bill):
    def total(self):
        return 1.18*Bill.total(self)
    
    #_total= total
    #__total=total

veg=[10,20,30]
g=Bill(veg)
print("Groceries Total",g.total())
print("Gorceries Cback",g.cashback())

food=[10,20,30]
r=GSTBill(food)
print("Groceries Total",r.total())
print("Gorceries Cback",r.cashback())
