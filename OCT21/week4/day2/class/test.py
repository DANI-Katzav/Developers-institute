#ex1:

my_fav_numbers = {10,7,18}
my_fav_numbers.add(20)
my_fav_numbers.add(22)
#print(my_fav_numbers)

my_fav_numbers.discard(22)
#print(my_fav_numbers)

friend_fav_number = {12,10,16,14}
#print(friend_fav_number)

our_fav_numbers = (my_fav_numbers | friend_fav_number)
#print(our_fav_numbers)