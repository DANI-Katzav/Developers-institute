


#1


print('hello world ' * 4)

#other way
hello = 'hello world '
print(hello * 4)

#ex2
res = (99^3) * 8
print(res)

#ex3
# >>> 5 < 3 false
# >>> 3 == 3 true
# >>> 3 == "3" false
# >>> "3" > 3 
# >>> "Hello" == "hello" false

#ex4

computer_brand = 'Dell'
print(f'I have a {computer_brand} computer')

#ex5
name = 'Danielle katzav'
age = 28
shoe_size = 39
Info = 'My name is {} and I am {}.  My shoes size is {}'.format(name, age, shoe_size)
print(Info)


#ex6
a = 5
b = 4
if a>b:
    print('Hello world')

#ex7:
number = int(input("Enter a number"))
if number%2 == 0:
    print('This number is even')
else:
    print('This number is odd')


#ex8
name_user = input('Enter you name').lower()

if  name_user == 'Danielle':
    print('Danielle is an Angel ')


#ex9

height_cm = int(input('Enter you height in inches'))
height_cm = height_cm * 2.54
if height_cm > 145:
    print('You are tall enough to ride')
else:
    print('You are not tall enough')

    








    