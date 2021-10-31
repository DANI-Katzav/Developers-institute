
my_dict_template = {
    'first_name': '',
    'last_name':'',
    'birth_date': ''
}
people = []
for num in range(0,3):
    person = my_dict_template.copy()
    for key in my_dict_template:
        info = input(f'please input this persons {key}')
        person[key] = info
    people.append(person)
print(people)


sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"

}
# keys_to_remove = ["name", "salary"]
for key in sample_dict:
    if key not in ['age', 'city']:
        del sample_dict[key]
print(sample_dict)

