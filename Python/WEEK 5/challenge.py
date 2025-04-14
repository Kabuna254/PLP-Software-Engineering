class Vehicle:
    def move(self):
        pass  

class Car(Vehicle):
    def move(self):
        print("Driving")

class Plane(Vehicle):
    def move(self):
        print("Flying")

class Bike(Vehicle):
    def move(self):
        print("Riding")

car = Car()
plane = Plane()
bike = Bike()

# Demonstrating polymorphism
for vehicle in [car, plane, bike]:
    vehicle.move() 
