class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def move(self):
       pass # Abstract method //overide but subclass

    def introduce(self):
        print(f"Hello, I am a {self.species} named {self.name}.")

class Dog(Animal):
    def move(self):
        print(f"{self.name} runs on four legs.")

class Cat(Animal):
    def move(self):
        print(f"{self.name} walks gracefully on four legs.")

class Bird(Animal):
    def move(self):
        print(f"{self.name} flies in the sky.")

print("\n -----Polymorphism----- \n")
animals =[
    Dog("Buddy", "Dog"),
    Cat("Whiskers", "Cat"),
    Bird("Tweety", "Bird")
]
for animal in animals:
    animal.introduce()  
    animal.move()
    print()