##ex1


print('hello world ' * 4)

# other way
hello = 'hello world '
print(hello * 4)

# ex2
res = (99 ^ 3) * 8
print(res)

# ex3
# >>> 5 < 3 false
# >>> 3 == 3 true
# >>> 3 == "3" false
# >>> "3" > 3
# >>> "Hello" == "hello" false

# ex4

computer_brand = 'Dell'
print(f'I have a {computer_brand} computer')

# ex5
name = 'Danielle katzav'
age = 28
shoe_size = 39
Info = 'My name is {} and I am {}.  My shoes size is {}'.format(name, age, shoe_size)
print(Info)

# ex6
a = 5
b = 4
if a > b:
    print('Hello world')

# ex7:
number = int(input("Enter a number"))
if number % 2 == 0:
    print('This number is even')
else:
    print('This number is odd')

# ex8
name_user = input('Enter you name').lower()

if name_user == 'Danielle':
    print('Dnielle is an Angel ')
else:

    # Exercise 9

    height_inches = int(input('Enter you height in inches'))
    height_cm = height_inches * 2.54
    if height_cm > 145:
        print('You are tall enough to ride')
    else:
        print('You need to grow some more to ride')

    # Write a code that receives 3 inputs and combines them:
    # A number input (integer, float etc.)
    # A number input (integer, float etc.)
    # A string, describing an operator (“add”, “multiply”, “divide”)
    # If the first two inputs are equal -> print number1 with the power of number2.
    # Otherwise, perform the 3rd input’s operator on number1 with number2 and print the result.
    # If the input from the user isn’t correct -> print an error message.

    while True:
        try:
            num_one = int(input('Enter a number'))
            num_two = int(input('Enter a number'))
            operator = input('Choose an operator: +, * or /')
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue

        if num_one == num_two:
            x = num_one ** num_two
            print(x)
        else:
            if operator == '+':
                print(num_one + num_two)
            elif operator == '*':
                print(num_two * num_one)
            elif operator == '/':
                print(num_one / num_two)
