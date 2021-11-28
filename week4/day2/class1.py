name = input('Whats your name?\n\t')
age = input('whats your age?')

if age.isnumeric() :
    age = int(age)
    if age != 0:
        print('we arent none')

else:
    print('stop throwing me letters instead of numbers')
    exit()

print('toby '  * age)


# intro_sen = 'hello my name is {}, i am {} years old'.format(name, age) # format is an old function
intro_sen2 = f'hello my name is {name}'

# print(intro_sen)
# print(intro_sen2)
intro_sen = 'hello my name is {} i am {} years old'.format(name, age) # format is an old function
print(intro_sen)

if age > 30 and name == 'toby':
    print('you arent that young toby')
elif age > 30 and name is not 'toby':
    print('you arent that young dude')
    
else:
    print('such a youngling')
    
print('we\'re done')


my_name = "Jack"
hello = "Hello World"
my_age = 27
my_list = [my_name, my_age, hello]

# List actions

# adding to a list
my_list += [1,2,3]
my_list.append('Toby')
my_list.insert(3, 'Value')

# removing from a list
item_to_remove = 1
my_list.remove(item_to_remove)
my_value = my_list.pop() # by default will remove the last item

# reassigning an item of a list
my_list[0] = 'My Favorite Exercise'

list1 = [5, 10, 15, 20, 25, 50, 20]
if 20 in list1:
    index = list1.index(20)
    list1[index] = 200
print(list1)

t1 = tuple(list1[0:2])
t2 = tuple(list1[2:])
print(t1)
print(t2)
num1, num2 = t1

print(num2)


f_name = input('whats your name? ')
l_name = input('whats your last name? ')
bday = input('whats your birthday? ')
info_tuple = (f_name, l_name, bday)
print(info_tuple)
name = info_tuple[0] + ' The Great' 
info_list = list(info_tuple)
print(info_list)

info_list[0] = name
print(info_list)
info_tuple = tuple(info_list)
print(info_tuple)

my_set = {1,2,3,6,6,6,4,5,6,6,6,6}
my_set2 = set()
my_list = list()
my_set.add('hello')
my_set.add('world')
print(my_set)
my_set.add(45)
num = my_set.pop()
print(num)
my_set_3 = {15,56,2}
my_set.update(my_set_3)
my_set | my_set_3 # adding two sets together (called a union)
print(my_set)