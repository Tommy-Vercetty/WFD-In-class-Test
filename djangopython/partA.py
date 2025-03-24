class Pet:

    def __init__(self, name, age, sex, petID, ownerName):
        self.name = name
        self.age = age
        self.sex = sex
        self.petID = petID
        self.ownerName = ownerName
    
    def updateName(self, updatedName):
        if isinstance(updatedName, str):
            self.name = updatedName
        else:
            print(f"{updatedName} is not a string")
    
    def updateAge(self, updatedAge):
        if isinstance(updatedAge, int):
            self.age = updatedAge
        else:
            print(f"{updatedAge} is not a valid integer")

    
    def updateSex(self, updatedSex):
        if isinstance(updatedSex, str):
            self.sex = updatedSex
        else:
            print(f"{updatedSex} is not a valid string")

    def updatePetID(self, updatedPetID):
        if isinstance(updatedPetID, int):
            self.petID = updatedPetID
        else:
            print(f"{updatedPetID} is not a valid integer")

    def updateOwnerName(self, updatedOwnerName):
        if isinstance(updatedOwnerName, str):
            self.ownerName = updatedOwnerName
        else:
            print(f"{updatedOwnerName} is not a valid string")
    
    def printPet(self):
        print(f"Name: {self.name}\n Age: {self.age}\n Sex: {self.sex}\n ID: {self.petID}\n Owner: {self.ownerName}")


pet1 = Pet("Fido", 4, "Male", 1, "Tommy")
pet1.printPet()

pet1.updateName("Midollo")
pet1.updateAge(10)
pet1.updateSex("Female")
pet1.updatePetID(5)
pet1.updateOwnerName("Fernando")

print("\n\n--- New Updated Pet ---\n")
pet1.printPet()

class Dog(Pet):
    def __init__(self, name, age, sex, petID, ownerName, tail, numberOfPaws):
        super().__init__(name, age, sex, petID, ownerName)
        self.tail = tail
        self.numberOfPaws = numberOfPaws
    
    def updatedTail(self, updatedTail):
        if isinstance(updatedTail, str):
            self.tail = updatedTail
        else:
            print(f"{updatedTail} is not a valid string")

    def updatedNumberOfPaws(self, updatedNumberOfPaws):
        if isinstance(updatedNumberOfPaws, int):
            self.numberOfPaws = updatedNumberOfPaws
        else:
            print(f"{updatedNumberOfPaws} is not a valid int")

    def printPet(self):
        super().printPet()
        print(f"Tail: {self.tail}\n Number of Paws: {self.numberOfPaws}")


print("\n\n--- Dog ---\n")
dog1 = Dog("Fufi", 21, "Male", 3, "Marco", "false", 4)
dog1.printPet()

dog1.updatedTail("true")
dog1.updatedNumberOfPaws(2)

print("\n\n--- New Updated Dog ---\n")
dog1.printPet()

class Cat(Pet):
    def __init__(self, name, age, sex, petID, ownerName, colour, animalSound):
        super().__init__(name, age, sex, petID, ownerName)
        self.colour = colour
        self.animalSound = animalSound

    def updatedColour(self, updatedColour):
        if isinstance(updatedColour, str):
            self.colour = updatedColour
        else:
            print(f"{updatedColour} is not a valid string")

    def updatedAnimalSound(self, updatedAnimalSound):
        if isinstance(updatedAnimalSound, str):
            self.animalSound = updatedAnimalSound
        else:
            print(f"{updatedAnimalSound} is not a valid string")

    def printPet(self):
        super().printPet()
        print(f"Colour: {self.colour}\n Animal Sound: {self.animalSound}")

cat1 = Cat("Bailey", 10, "Female", 12, "Vitaliy", "Orange", "Miaw")
print("\n\n--- Cat ---\n")
cat1.printPet()

cat1.updatedColour("Black")
cat1.updatedAnimalSound("Wof Wof")

print("\n\n--- New Updated Cat ---\n")
cat1.printPet()