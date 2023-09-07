from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def talk(self):
        pass

class Dog(Animal):
    def talk(self):
        return 'woof woof'

class Cat(Animal):
    def talk(self):
        return 'meow'

def say_hi(animal):
    return animal.talk()


dog1 = Dog('Buddy')
cat1 = Cat('Garfield')


print(say_hi(dog1))  
print(say_hi(cat1))  
