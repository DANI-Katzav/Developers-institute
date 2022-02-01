
#ex1
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age


def oldest_cat(cat_list):
    # max([cat.age for cat in cat_list])
    return sorted(cat_list, key=lambda cat:cat.age, reverse=True)[0]

def oldest_longer(cat_list):
    age = cat_list[0].age
    current_cat = cat_list[0]
    for cat in cat_list:
        if cat.age > age:
            current_cat = cat
    return current_cat


data_list = [('rex', 34), ('mr bubbles', 12), ('meowscules', 8)]
cats = [Cat(*data) for data in data_list]
oldest = oldest_cat(cats)
print(oldest.name, oldest.age)
oldest = oldest_longer(cats)
print(oldest.name, oldest.age)




#ex2
class Animal:
    def __init__(self, name, legs=None):
        self.name = name
        self.legs = legs
        self.walk()
        
    def walk(self):
        if self.legs:
            print(f'the animal {self.name} walks on {self.legs} feet')
        else:
            print('no legs for walking')

class Dog(Animal):
    def bark(self):
        print(f"{self.name} barked, WAF !")

animal = Animal('Frog', 4)
animal2 = Animal('Fish')
dog1 = Dog('Sparky', 4)


# dog1.bark()

class Animal:
    def __init__(self, animal_type, number_legs, sound):
        self.animal_type = animal_type
        self.number_legs = number_legs
        self.sound = sound

    def make_sound(self):
        print(f"I am an animal, and I love saying {self.sound}")

class Dog(Animal):
    def __init__(self, animal_type, number_legs, sound, is_old, age):
        super().__init__(animal_type, number_legs, sound)
        self.age = age
        self.is_old = is_old



    def fetch_ball(self):
        print("I am a dog, and I love fetching balls")

    def make_sound(self):
        super().make_sound()
        print('doggy go woof!')



animal = Animal("cat", 4, "purr")
rex= Dog("dog", 4, "wouaf", True, 15)
print('This animal is a:', rex.animal_type)

print('This dog has', rex.number_legs , ' legs')
print('This dog makes the sound ', rex.sound)
rex.make_sound()
rex.fetch_ball()
animal.make_sound()
# animal.fetch_ball()
