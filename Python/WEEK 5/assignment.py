# Parent class with private and protected attributes
class Playstation:
    def __init__(self, model, orientation):
        self.__model = model         # private
        self._orientation = orientation  # protected

    def get_model(self):
        return self.__model

    def set_model(self, model):
        self.__model = model.lower()

    def game(self):
        print("Generic PlayStation gaming...")

# Child class for PS4
class PS4(Playstation):
    def __init__(self):
        super().__init__("ps4", "horizontal")

    def game(self):
        print("Playing on PS4 - horizontal setup ")

# Child class for PS5
class PS5(Playstation):
    def __init__(self):
        super().__init__("ps5", "vertical")

    def game(self):
        print("Playing on PS5 - vertical setup ")

# Create PlayStations
ps1 = PS4()
ps2 = PS5()

# Access and change private/protected data
print(ps1.get_model())      # Access private model
print(ps2._orientation)     # Access protected orientation

ps1.set_model("ps5")        # Change model using setter
print(ps1.get_model())      # Confirm change

# Polymorphism in action
for ps in [ps1, ps2]:
    ps.game()
