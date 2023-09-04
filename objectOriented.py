
class Animal:
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

# Create instances of classes.
my_dog = Dog("Max", "Canine")
my_cat = Cat("Moon", "Feline")

# Call instance methods
print(f"{my_dog.name} does: {my_dog.make_sound()}")
print(f"{my_cat.name} does: {my_cat.make_sound()}")
