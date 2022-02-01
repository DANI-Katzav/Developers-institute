
fruits = ['apple', 'banana', 'kiwi', 'pear']

for fruit in fruits:
    print(fruit)

cities = ["Tel Aviv", "San Francisco", "Paris", "Barcelona"]

for city in cities[0:2]:
    print("I once went to", city)
import random

total = 0
for number in range(0,100):
    if number == 45:
        continue
    total += number

print(total)
numbers = list(range(0,1000))
random.shuffle(numbers)
print(numbers)

lowest = numbers[0]
for number in numbers:
    if number < lowest:
        lowest = number
    if number == 80:
        print('im done')
        break

        
print(lowest)


user_number = input('Please give me a number')

while (not user_number.isnumeric()) or user_number == '0':
    print('that aint a number')
    user_number = input('Please give me a number')


for num in range(1,11):
    print(int(user_number)*num)


while True: 
    city = input("Please enter the name of a city you have visited (enter 'quit' when you are finished): ")
    if city in ['quit', 'leave me alone', 'stop']:
        break
    else:
        print("I'd love to go to", city)

print("Goodbye !")


current_number = 1 
while current_number <= 5:    
    print(current_number)   
    current_number += 1

print("Finished")



user_input = input('Please give a string 10 chars long')
while len(user_input) < 10 or len(user_input) > 10:
    if len(user_input) < 10:
        print('string not long enough')
    elif len(user_input) > 10:
        print('string too long')
    user_input = input('Please give a string 10 chars long')


print(user_input[0], user_input[-1])

current_string = ''

for char in user_input:
    current_string += char
    print(current_string)

letters = list(user_input)
letters2 = random.shuffle(letters)
print(letters2)
print("".join(letters))