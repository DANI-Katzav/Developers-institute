my_age = 29
new_age = my_age + 123879
print(new_age)

first_name = "Daniele"
last_name = " katzav"
print(first_name + last_name)

cars = 100  # int
space_in_a_car = 4.0  # float
drivers = 30  # int
passengers = 90  # int
cars_not_driven = cars - drivers  # 70
cars_driven = drivers  # 30
carpool_capacity = cars_driven * space_in_a_car  # 30*4/0
average_passengers_per_car = passengers / cars_driven  # 3

userNum = int(input("Enter a number between 1 and 100: "))

if (userNum % 3 == 0) and (userNum % 5 == 0):
    print("FizzBuzz")
elif userNum % 5 == 0:
    print("Buzz")
elif userNum % 3 == 0:
    print("Fizz")
