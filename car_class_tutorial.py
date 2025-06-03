# Tutorial Assignment 1: Classes and Objects in Python
class Car:
    
    def __init__(self, brand, model, color):
        self.brand = brand  # Attribute
        self.model = model  # Attribute
        self.color = color  # Attribute

    
    def display_info(self):
        print(f"Car Brand: {self.brand}, Model: {self.model}, Color: {self.color}")


car1 = Car("Toyota", "Corolla", "Red")
car2 = Car("Tesla", "Model S", "Blue")


car1.display_info()
car2.display_info()
