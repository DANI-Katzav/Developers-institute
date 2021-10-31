class Person():
  def __init__(self, name, age):
    self.name = name
    self.age = age

first_person = Person("John", 36)

print(first_person.name) #jhon
print(first_person.age)#36

#Explain the goal of the `__init__()` method

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

## create an instance of the class
p = Point(3,4)

## access the attributes
print("p.x is:", p.x) #p.x is:3
print("p.y is:", p.y) #p.y is:4


class Dog():
    # Initializer / Instance Attributes
    def __init__(self, name_of_the_dog):
        print("A new dog has been initialized !")
        print("His name is", name_of_the_dog)
        self.name = name_of_the_dog

    def bark(self):
        print("{} barks ! WAF".format(self.name))

        dog1 = Dog('rex')
        print(dog1.name)
        dog1.bark()
        dog1.walk('100')
        dog1.rename('tobi')
        print(dog1)




