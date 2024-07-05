class Animal:
    animalType="Mammals"

class Pets(Animal):
    color ="White"

class Dog(Pets):
    @staticmethod
    def bark():
        print("bow bow!")

d =Dog()
print(d.bark())