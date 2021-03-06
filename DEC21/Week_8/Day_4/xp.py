

# Exercise 1 : Pets

class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Persan(Cat):
    def sing(self, sounds):
        return f'{sounds}'


cat1 = Persan('miau',4)
cat2 = Chartreux('kity',20)
cat3 = Bengal('lola',7)

my_cats = [cat1,cat2,cat3]
my_pets = Pets(my_cats)
my_pets.walk()

# Exercise 2 : Dogs

class Dog:
    def __init__(self,name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
    
    def bark(self):
        return f'{self.name} is barking'
    
    def run_speed(self):
        self.speed = self.weight/self.age*10
        return self.speed
    
    def fight(self,other_dog):
        if (self.weight * self.speed) > (other_dog.weight * other_dog.speed):
            return f'{self.name} is the winner'
        elif (self.weight * self.speed) < (other_dog.weight * other_dog.speed):
            return f'{other_dog.name} is the winner'
        else:
            return f'There is not a winner'

dog1 = Dog('fox', 32, 58)
dog2 = Dog('dogi',15,35)
dog3 = Dog('nemo',6,15)

print(dog1.bark())
print(dog2.bark())
print(dog3.bark())

print(dog1.run_speed())
print(dog2.run_speed())
print(dog3.run_speed())

print(dog1.fight(dog2))
print(dog2.fight(dog3))
print(dog3.fight(dog1))


# Exercise 3 : Dogs Domesticated
import random

class PetDog(Dog):
    def __init__(self,name, age, weight, trained=False):
        super().__init__(name,age,weight)
        self.trained = trained
    
    def train(self):
        self.trained = True
        return super().bark()
    


    def do_a_trick(self):
        order = [f'{self.name} does a barrel roll',f'{self.name} stands on his back legs',f'{self.name} shakes your hand',f'{self.name} plays dead']
        print(random.choice(order))
    
dog1 = Dog('fox', 32, 58)
dog2 = Dog('dogi',15,35)
dog3 = Dog('nemo',6,15)

