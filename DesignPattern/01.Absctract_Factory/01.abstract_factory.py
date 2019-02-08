class PetShop:
    def __init__(self, animal_facotry=None):
        self.pet_factory = animal_facotry

    def show_pet(self):
        pet = self.pet_factory.get_pet()
        print("This is a lovely", pet)

class Dog:
    def speak(self):
        return "woof"

    def __str__(self):
        return "dog"

class Cat:
    def speak(self):
        return "meow"

    def __str__(self):
        return "cat"

class DogFactory:
    def get_pet(self):
        return Dog()

class CatFactory:
    def get_pet(self):
        return Cat()


if __name__ == "__main__":
    shop = PetShop()
    shop.pet_factory = CatFactory()
    shop.show_pet()