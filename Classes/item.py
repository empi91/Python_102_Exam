# item.py

class Item:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.name}"

    def use_item(self):
        print(f"{self.name} used")

    def take_item(self):
        print(f"{self.name} taken")

    def throw_item(self):
        print(f"{self.name} thrown")