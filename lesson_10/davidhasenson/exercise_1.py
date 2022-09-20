class Animal:

    def __init__(self, name):
        self.name = name

    def name_doubel(self):
        return self.name *2

class Dog(Animal):

    def __init__(self, name):
        self.name = name

    def name_doubel(self):
        return self.name *4

def main():
    animal_one = Animal("max")
    print(animal_one.name_doubel())
    dog_one = Dog("jonas")
    print(dog_one.name_doubel())

if __name__=="__main__":
    main()