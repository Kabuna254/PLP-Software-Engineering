class Playstation:
    def __init__(self, model, orientation):
        self.model = model
        self.orientation = orientation

    def game(self):
        if self.model == "ps4":
            print("My playstation is a ps4 with a horizontal orientation")
        elif self.model == "ps5":
                print("My playstation is a ps5 with a vertical orientation")
        else:
            print("Error")


first_ps = Playstation("ps4", "horizontal")
second_ps = Playstation("ps5", "vertical")

print(first_ps.model)
print(second_ps.orientation)
first_ps.game()
second_ps.game()