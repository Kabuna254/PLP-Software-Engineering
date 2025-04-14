# defining a class
class Car:
    color = "red" # attribute
    model = "audi"
    make = "2021"

    # method
    def drive(self):
        print("The car is driving")

# creating an object
my_car = Car()
print(my_car.color, my_car.model, my_car.make)
my_car.drive()

class Cab:
    def __init__(self, color, model):
        self.color = color # instance variable
        self.model = model # instance variable

# creating objects with unique attributes
cab1 = Cab("blue", "sedan")
cab2 = Cab("red", "suv")
print(cab1.color)
print(cab2.model)

class Vehicle:
    def __init__(self, wheels):
        self.wheels = wheels

class Car(Vehicle):
    pass

car = Car(4)
print(car.wheels)  # Output: 4


# POLYMORPHISM
class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

# Polymorphism in action
for animal in [Dog(), Cat()]:
    print(animal.speak())

# Encapsulation
class SecretStash:
    def __init__(self):
        self.__chocolates = 10  # Private attribute

    def take_chocolate(self):
        if self.__chocolates > 0:
            self.__chocolates -= 1
            print("One chocolate taken!")
        else:
            print("No chocolates left 😢")

stash = SecretStash()
stash.take_chocolate()