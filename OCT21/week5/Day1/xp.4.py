

#ex.4

class Zoo:
    def __init__(self,zoo_name):
        self.name = zoo_name
        self.animals = []


    def add_animal(self, new_animal):
        '''This method adds the new_animal 
        to the animals list as long as it isn't already in the list.'''
        if not new_animal in self.animals:
            self.animals.append(new_animal)
    
    def get_animals(self):
        '''prints all the animals of the zoo.'''
        for animal in self.animals:
            print(animal)

    def sell_animal(self, animal_sold):
        '''removes the animal from the list if it exists in the list.'''
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)

    def sort_animals(self):
        '''Create a method called sort_animals that sorts the animals
         alphabetically and groups them together based on their first letter.'''
        animals_lists = []
        # print(self.animals)
        # print(sorted(self.animals))
        for animal in sorted(self.animals):
            # print('current animal:', animal)
            if not animals_lists:
                animals_lists.append([animal])
                
            else:
                # print(f"current animal first letter: {animal[0]}")
                # print(f"last list: {animals_lists[-1]}")
                # print(f"first object in last list: {animals_lists[-1][0]}")
                # print(f"first letter of first object in last list: {animals_lists[-1][0][0]}")
                if animal[0] == animals_lists[-1][0][0]:
                    # print('matches last object')
                    animals_lists[-1].append(animal)
                else:
                    animals_lists.append([animal])
                

            
            # print(animals_lists)
        animals_sorted = {}
        for index, sublist in enumerate(animals_lists):
            # print('the current sublist:', sublist)
            # print('sublist[0]', sublist[0])
            if len(sublist) == 1:
                animals_sorted[index+1] = sublist[0]
            else:
                animals_sorted[index+1] = sublist

        print(animals_sorted)



ramat_gan_safari = Zoo('Ramat Gan Safari')
for animal in ['Cat', 'Cougar',"Baboon", 'Eel', 'Emu',"Baboon","Baboon","Baboon", "Bear", "Ape",]:
    ramat_gan_safari.add_animal(animal)

ramat_gan_safari.sort_animals()


#ex.4 avi in class

class Zoo:
    def __init__(self,zoo_name):
        self.name = zoo_name
        self.animals = []


    def add_animal(self, new_animal):
        '''This method adds the new_animal 
        to the animals list as long as it isn't already in the list.'''
        if not new_animal in self.animals:
            self.animals.append(new_animal)
    
    def get_animals(self):
        '''prints all the animals of the zoo.'''
        for animal in self.animals:
            print(animal)

    def sell_animal(self, animal_sold):
        '''removes the animal from the list if it exists in the list.'''
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)

    def sort_animals(self):
        '''Create a method called sort_animals that sorts the animals
         alphabetically and groups them together based on their first letter.'''
        animals_lists = []
        for animal in sorted(self.animals):
            if not animals_lists:
                animals_lists.append([animal])
                
            else: 
                if animal[0] == animals_lists[-1][0][0]:
                    animals_lists[-1].append(animal)
                else:
                    animals_lists.append([animal])
            
        animals_sorted = {
            index+1: sublist[0] if len(sublist) == 1 else sublist 
            for index, sublist in enumerate(animals_lists)
            }
        
        print(animals_sorted)



ramat_gan_safari = Zoo('Ramat Gan Safari')
for animal in ['Cat', 'Cougar',"Baboon", 'Eel', 'Emu',"Baboon","Baboon","Baboon", "Bear", "Ape",]:
    ramat_gan_safari.add_animal(animal)

ramat_gan_safari.sort_animals()


