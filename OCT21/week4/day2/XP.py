#ex1:

my_fav_numbers = {10,7,18}
my_fav_numbers.add(20)
my_fav_numbers.add(22)


my_fav_numbers.discard(22)


friend_fav_number = {12,10,16,14}


our_fav_numbers = (my_fav_numbers | friend_fav_number)


#ex2:

#Given a tuple which value is integers,
 #is it possible to add more integers to the tuple?

#no .you need to do new tuple

#ex3:
for i in range(1,21):
    print(i)


#ex4:
my_list = []
start = 1
while start < 5:
    start += 0.5
    my_list.append(start)
print(my_list)

#ex5:
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove('Banana') 
basket.remove('Blueberries') 
basket.append('Kiwi') 
basket.insert(0,'Apples')

count = 0
for fruits in basket:
    if fruits == 'Apples':
        count += 1
print(count)

basket.clear()
print(basket)


#ex6:



 wrong_name = True
 while wrong_name:
    name = input("Enter a name")
     if name == "Danielle Katzav":
         wrong_name=False
     else:
         print('not my name')
    print('my name')


# Exercise 7
my_list2 = list(range(0,20,2))
print(my_list2)
for i in my_list2:
    if my_list2.index(i)%2==0:
        print(i)

# Exercise 8
for i in list(range(1500,2501)):
    if i%5==0 and i%7==0:
        print(i)


#ex9
fruits = input('Enter your favorite fruit(s) separate with single space')

s_fruits = fruits.split(' ')  
print(s_fruits)

name_fruit = input('Enter name of a fruit')

if name_fruit in fruits:
    print('You chose one of your favorite fruits! Enjoy!')
else:
    print("You chose a new fruit. I hope you enjoy")


# Ex10
toppings = []
while True:
    user_choice = input('Enter a topping, when you want to stop input quit')
    if user_choice== 'quit':
        break
    else:
        toppings.append(user_choice)

print(toppings)
price = len(toppings)*2.5+10
print(f"The price of the pizza is: {price}")


#ex11

price = 0
while True:
    age = input('Enter your age and when it finish input quit')
    if age == 'quit':
        break
    elif 2<int(age)<13:
        price+=10
    elif int(age)>12:
        price+= 15
    elif int(age) <3:
        price +=0
print(price)


teens_allowed=[]
while True:
    age = input('Enter your age and when it finish input quit')
    if age == 'quit':
        break
    elif 15<int(age)<22:
        name = input('Enter your name')
        teens_allowed.append(name)
    else:
        print('You can\'t see the moovie')
print(teens_allowed)


# Ex12
name_list = ['lea', 'tom','sarah', 'shana','mickael','sam']
name_under = []
for i in name_list:
    age = input("Enter your age")
    if int(age) <16:
        name_under.append(i)

for j in name_under:
    name_list.remove(j)


print(name_list)



# Ex13
sandwich_orders = ['american', 'kebab','burger']
finished_sandwiches=[]

for i in sandwich_orders:
    print(f'I made you {i} sandwich')
    finished_sandwiches.append(i)

print(finished_sandwiches)


# Ex14
sandwich_orders = ['american', 'kebab','burger']
finished_sandwiches=[]
pastrami_order = ['pastrami','pastram','pastram']
sandwich_orders+=pastrami_order
print(sandwich_orders)

for i in sandwich_orders:
    if i== 'pastram':
        print('the deli has run out of pastrami')

while 'pastram' in sandwich_orders:
    sandwich_orders.remove('pastram')

print(sandwich_orders)

for i in sandwich_orders:
    print(f'I made you {i} sandwich')
    finished_sandwiches.append(i)

print(finished_sandwiches)

