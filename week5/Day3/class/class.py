class Person:
    people = []


    def __init__(self, fname, lname, age):
        self.first_name = fname
        self.last_name = lname
        self.age = age
        self.favorite_foods = []
        self.people.append(self)
    
    def __str__(self):
        return (self.first_name + ' ' + self.last_name).title()

    def __repr__(self):
        return f'person object: {self}'

    def __int__(self):
        return self.age
    
    def __call__(self):
        return 'check me out i was called'
    
    def __gt__(self, other):
        if isinstance(other, int):
            return self.age > other
        elif isinstance(other, float):
            return self.age > other
        elif isinstance(other, Person):
            return self.age > other.age
        else:
            raise Exception('this operation is not supported, we only compare people to person, int or float')

    def __lt__(self, other):
        if isinstance(other, int):
            return self.age > other
        elif isinstance(other, float):
            return self.age > other
        elif isinstance(other, Person):
            return self.age > other.age
        else:
            raise Exception('this operation is not supported, we only compare people to person, int or float')

p1 = Person('Toby', 'Tobuscus', 45)
p2 = Person('CJ', 'Craigg', 45)
p3 = Person('The', 'Doctor', 890)
print(p1)
print(p2)
print(p3)

print(p1 > p2)