from typing import List

class Human:

	def __init__(self, name: str, age: int, living_place=None):
		self.name = name
		self.age = age
		self.living_place = living_place

	def move(self, new_building):
		# remove from current building.
		# if self.living_place != None:
		if self.living_place:
			self.living_place.remove_inhabitant(self)

		self.living_place = new_building
		new_building.inhabitants.append(self)


class Building:

	def __init__(self, address: str, inhabitants: List[Human]):
		self.address = address
		self.inhabitants = inhabitants

	def show_inhabitants_info(self):
		for inhabitant in self.inhabitants:
			print(inhabitant.name, inhabitant.age)

	def remove_inhabitant(self, inhabitant: Human):
		self.inhabitants.remove(inhabitant)

	def get_number_of_inhabitants(self):
		return len(self.inhabitants)

	def get_total_ages_of_inhabitants(self):
		total_ages = 0

		for inhabitant in self.inhabitants:
			total_ages += inhabitant.age

		return total_ages


class City:

	def __init__(self, name: str, buildings: List[Building]):
		self.name = name
		self.buildings = buildings

	def construct(self, address):
		new_building = Building(address, [])
		self.buildings.append(new_building)

	def info(self, address):
		counter = 0
		total_ages_of_humans = 0
		number_of_humans = 0

		for building in self.buildings:
			if building.address == address:
				counter += 1
				number_of_humans += building.get_number_of_inhabitants()
				total_ages_of_humans += building.get_total_ages_of_inhabitants()

		mean = total_ages_of_humans / number_of_humans

		print(f"the number of building at the address {address} is {counter}")
		print(f"the mean age of the citizens at the address {address} is {mean}")


building1 = Building("st", [])
building2 = Building("bre", [])
building3 = Building("st", [])

avi = Human("avi", 50)
rick = Human("rick", 65)
rick2 = Human("rick2", 39)

avi.move(building1)
rick.move(building1)
rick2.move(building3)

tlv = City("TLV", [building1, building2, building3])
tlv.info("st")



# print(building1.inhabitants)
# building1.show_inhabitants_info()
# rick.move(building2)