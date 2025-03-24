import unittest
from partA import Pet, Dog, Cat

class UnitTest(unittest.TestCase):
    
    def setUp(self):
        self.pet = Pet("Fido", 4, "Male", 1, "Tommy")
        self.pet1 = Pet("Fido", 4, "Male", 1, "Tommy")
        self.dog = Dog("Fufi", 21, "Male", 3, "Marco", "false", 4)
        self.cat = Cat("Bailey", 10, "Female", 12, "Vitaliy", "Orange", "Miaw")

    def test_petIsInstance(self):
        self.assertIsInstance(self.pet, Pet)

    def test_petIsNotInstance(self):
        self.assertNotIsInstance(self.pet, Dog)


    def test_dogIsInstance(self):
        self.assertIsInstance(self.dog, Dog)
        self.assertIsInstance(self.dog, Pet)

    def test_dogIsNotInstance(self):
        self.assertNotIsInstance(self.dog, Cat)
        self.assertNotIsInstance(self.dog, Pet)


    def test_catIsInstance(self):
        self.assertIsInstance(self.cat, Cat)
        self.assertIsInstance(self.cat, Pet)
    
    def test_catIsNotInstance(self):
        self.assertNotIsInstance(self.cat, Dog)
        self.assertNotIsInstance(self.cat, Pet)


    def test_objectsAreSame(self):
        self.assertIs(self.pet, self.pet1)
    
    def test_objectsArentSame(self):
        self.assertIsNot(self.pet1, self.dog)


    def test_nameValid(self):
        self.pet.updateName("Bobby")
        self.assertEqual(self.pet.name, "Bobby")
    
    def test_nameInvalid(self):
        with self.assertRaises(ValueError):
            self.pet.updateName(123)
    

    def test_ageValid(self):
        self.pet.updateAge(5)
        self.assertEqual(self.pet.age, 5)
    
    def test_ageInvalid(self):
        with self.assertRaises(ValueError):
            self.pet.updateAge("Twenty")


    def test_sexValid(self):
        self.pet.updateSex("Female")
        self.assertEqual(self.pet.sex, "Female")
    
    def test_sexInvalid(self):
        with self.assertRaises(ValueError):
            self.pet.updateSex(15)
    

    def test_petIDValid(self):
        self.pet.updatePetID(2)
        self.assertEqual(self.pet.petID, 2)
    
    def test_petIDInvalid(self):
        with self.assertRaises(ValueError):
            self.pet.updatePetID("Two")
    
    def test_ownerNameValid(self):
        self.pet.updateOwnerName("Mattia")
        self.assertEqual(self.pet.ownerName, "Mattia")
    
    def test_ownerNameInvalid(self):
        with self.assertRaises(ValueError):
            self.pet.updateOwnerName(456)

    def test_tailValid(self):
        self.dog.updatedTail("True")
        self.assertEqual(self.dog.tail, "True")

    def test_tailInvalid(self):
        with self.assertRaises(ValueError):
            self.dog.updatedNumberOfPaws(2)

    def test_numberOfPawsValid(self):
        self.dog.updatedNumberOfPaws(4)
        self.assertEqual(self.dog.tail, 4)

    def test_numberOfPawsInvalid(self):
        with self.assertRaises(ValueError):
            self.dog.updatedNumberOfPaws("Two")

    def test_colourValid(self):
        self.cat.updatedColour("White")
        self.assertEqual(self.cat.colour, "White")

    def test_colourInvalid(self):
        with self.assertRaises(ValueError):
            self.cat.updatedColour(13)

    def test_animalSoundValid(self):
        self.cat.updatedAnimalSound("Beeeh")
        self.assertEqual(self.cat.animalSound, "Beeeeh")

    def test_animalSoundInvalid(self):
        with self.assertRaises(ValueError):
            self.cat.updatedAnimalSound(21)
    

if __name__ == '__main__':
    unittest.main()
