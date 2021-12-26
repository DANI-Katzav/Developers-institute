


class Person:
    def __init__(self,id, firstname, lastname):
        self.id = id
        self.firstname= firstname
        self.lastname= lastname
    def say_my_name(self):
        print("my name is " + self.firstname )

person1 = Person(308516616, "danielle", "katzav")                    
print(person1.id)
person1.say_my_name()

person2 = Person(1234, "dan", "bekker")
print(person2.id)
person2.say_my_name()


class Car:
    def __init__(self,model, price):
        self.model = model
        self.price = price
    def in_shekels(self):
        print("the price in NIS is " + str(self.price * 3.12))

car1 = Car("bmw", 200)
car1.in_shekels()
car2 = Car("Toyota", 100)
