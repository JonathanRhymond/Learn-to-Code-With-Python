class Pokemon():
    def __init__(self, name, specialty, health=100):
        self.name = name
        self.specialty = specialty
        self.health = health

    def roar(self):
        print("Roar!")

    def describe(self):
        print(f"I am {self.name}. I am a {self.specialty} Pokemon!")
    
    def take_damage(self, amount):
        self.health -= amount

squritle = Pokemon("Squritle", "Water")
charmander = Pokemon(name = "Charmander", specialty = "Fire", health = 110)

squritle.roar()
charmander.roar()

squritle.describe()
charmander.describe()

print(squritle.health)
squritle.take_damage(20)
print(squritle.health)

squritle.health = 60
print(squritle.health)

print(charmander.health)