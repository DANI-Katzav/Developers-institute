#
# class Door:
#
# 	objs = 0
# 	list_of_doors = [] # [ d0, d1, d2, d3 ]
#
# 	def __init__(self, locked):
# 		Door.list_of_doors.append(self)
# 		Door.objs += 1
#
# 		self.id = Door.objs
# 		self.locked = locked
#
# 	@property
# 	def next(self):
# 		return Door.list_of_doors[self.id:]
#
# 	def can_go_to(self, other_door):
# 		next_doors = self.next # [d2, d3]
#
# 		for i in range(len(next_doors)):
#
# 			if next_doors[i].locked == False:
# 				return False
#
# 			# did I reached to the destination door
# 			if next_doors[i] == other_door:
# 				return True
#
# 		return False
#
#
# d1 = Door(True)
#
# """
# objs = 1
# list_of_doors = [ d1 ]
# """
#
# d2 = Door(True)
# """
# objs = 2
# list_of_doors = [ d1, d2 ]
# """
#
# d3 = Door(True)
# """
# objs = 3
# list_of_doors = [ d1, d2, d3 ]
# """
#
# print(d1.next)
# print("d1 --> d3", d1.can_go_to(d3))
#
#
# # | | | |
#
# print(d1 == d1)
# print(d1 == d2)

class Door:

    objs = 0
    num_of_doors = []


    def __init__(self,locked=False):
        Door.objs += 1
        Door.num_of_doors.append(self)
        self.id = Door.objs
        self.locked = locked

    @property
    def next_door(self):
        return Door.num_of_doors[self.id:]

    def can_enter_door(self,other_door):
        if self.locked == other_door.locked:
            return True






door1 = Door(True)
door2 = Door(False)
door3 = Door(True)
door4 = Door(False)

print(door1.next_door)
print(door2.next_door)
print(door3.next_door)

print(door1.can_enter_door(door3))



print(door1.id)
