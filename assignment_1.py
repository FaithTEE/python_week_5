class superhero:
    def __init__(self, secret_identity,name, superpower, weakness, energy):
        self.name = name
        self.secret_identity = secret_identity
        self.superpower = superpower
        self.energy =  100
        self.weakness = weakness
        
    def use_power(self):
        if self.energy >=15:
            print(f"{self.name} uses {self.superpower}!")
            self.energy -= 10
        else:
            print(f"{self.name} is too tired to use their power!")

    def recharge(self):
        if self.energy < 100:
            print(f"{self.name} is recharging...")
            self.energy += 10
        else:
            print(f"{self.name} is already at full energy!")

    def introduce(self):
        print(f"Hello, I am {self.name}, also known as {self.secret_identity}.")
        print(f"My superpower is {self.superpower} and my weakness is {self.weakness}.")
        print(f"I have {self.energy} energy points left.")

class villain:
    def __init__(self, secret_identity,name, evil_plan, weakness, energy):
        self.name = name
        self.secret_identity = secret_identity
        self.evil_plan = evil_plan
        self.energy =  100
        self.weakness = weakness
        
    def use_power(self):
        if self.energy >=15:
            print(f"{self.name} uses {self.evil_plan}!")
            self.energy -= 10
        else:
            print(f"{self.name} is too tired to use their power!")

    def recharge(self):
        if self.energy < 100:
            print(f"{self.name} is recharging...")
            self.energy += 10
        else:
            print(f"{self.name} is already at full energy!")

    def introduce(self):
        print(f"Hello, I am {self.name}, also known as {self.secret_identity}.")
        print(f"My evil plan is {self.evil_plan} and my weakness is {self.weakness}.")
        print(f"I have {self.energy} energy points left.")

# Example usage
if __name__ == "__main__":
    hero = superhero("Clark Kent", "Superman", "Flight", "Kryptonite", 100)
    villain = villain("Lex Luthor", "Lex Luthor", "World Domination", "Superman", 100)

    hero.introduce()
    villain.introduce()

    hero.use_power()
    villain.use_power()

    hero.recharge()
    villain.recharge()

    hero.introduce()
    villain.introduce()