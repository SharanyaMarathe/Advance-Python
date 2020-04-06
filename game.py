from cars import Car

zen = Car(100,300,10)
print("Mileage", zen.get_mileage())
#print("Car color: ",zen.base_clr)
print("Car color: ",zen.color)
zen.start=400
print("cheat:",zen.get_mileage())
zen.end=400
print("finding mileage")
print("New mileage",zen.get_mileage())
zen.end=200
print("finding mileage")
print("New mileage",zen.get_mileage())
