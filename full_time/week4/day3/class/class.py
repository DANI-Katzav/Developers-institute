a_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}

print(a_dict.items())
# output : 
#dict_items([('color', 'blue'), ('fruit', 'apple'), ('pet', 'dog')])


# The items() method returns a view object that displays 
# a list of dictionary's (key, value) tuple pairs.


for key, value in a_dict.items():
    print(key, '->', value)

# output
#color -> blue
#fruit -> apple
#pet -> dog 



my_dog = {
  'name': 'Rufus',
  'age': 4,
  'best_friend': {
    'name': 'Felix',
    'age': 4.5
  },
  'favorite_foods': ['steaks', 'sausages', 'shawarma']
}

my_dog['best_friend']['name']


sample_dict = { 
   "class":{ 
      "student":{ 
         "name":"Mike",
         "marks":{ 
            "physics":70,
            "history":80
         }
      }
   }
}

print(sample_dict['class']['student']['marks']['history'])
print(sample_dict['class']['student']['marks']['physics'])

a_list = [2,3,4,12,57]

print(3 in a_list)