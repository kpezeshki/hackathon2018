import time, random

RACK_SIZE = 5

lockIDs = {} #lockIDs keeps a record of which position in the rack a given id has reserved
rackSlots = [] #rackSlots keeps a record of which slots in the rack are empty and full

class Slot:

	def __init__(self, position):
		self.isLocked = False
		self.position = position
		self.isClaimed = False
		self.studentIDNum = None
		#self.hasBoard = False
		#self.isHingeOpen = False

	def claim(self, id):
		#checks whether or not the slot physically has a board in it
		#if self.hasBoard == False:

		#unlocks the solenoid
		unlock_solenoid(self.position)

		#waits while the user opens the rack and inserts the board
		while isHingeOpen(self.position) == False:
			time.sleep(0.1)

		#once the rack is re-closed, the states will update
		if isHingeOpen(self.position) == True: 
			self.isClaimed = True
			self.isLocked = True
			self.studentIDNum = id
			lock_solenoid(self.position)

	def unclaim(self):
		#Checks whether or not the slot physically has a board in it
		#if self.hasBoard = True:

		#unlocks the solenoid
		unlock_solenoid(self.position)

		#waits for the user to open the door
		while isHingeOpen(self.position) == False:
			time.sleep(0.1)

		#once the rack is re-closed, the states will update
		if isHingeOpen(self.position) == False: 
			self.isClaimed = False
			self.isLocked = False
			self.studentIDNum = None
			lock_solenoid(self.position)

	def __repr__(self):
		printstr = ""
		printstr += "(Position " + str(self.position)

		if self.isClaimed == True:
			printstr += " claimed by " + str(self.studentIDNum)
		else:
			printstr += " unclaimed"
		printstr += ")"
		return printstr


racks = [Slot(i) for i in range(RACK_SIZE)]

def find_open_rack_pos():
	for slot in racks:
		if slot.isClaimed == False:
			return slot.position

def add_board(id):
	slot = racks[find_open_rack_pos()]
	slot.claim(id)
	print("rack", slot, "claimed")

def find_rack(id):
	for slot in racks:
		if slot.studentIDNum == id:
			return slot

def remove_board(id):
	slot = find_rack(id)
	slot.unclaim()
	print("rack", slot, "unclaimed")

def print_rack():
	for slot in racks:
		print(slot)

def isHingeOpen(position):
	limitSwitchInput = random.getrandbits(1)	 
	if (limitSwitchInput > 0): #on
		return True
	else: #off
		False
	pass
def lock_solenoid(num):
	pass
def unlock_solenoid(num):
	pass
def hasBoard(ultrasonicSensorInput):
	pass

add_board("test")
print(find_open_rack_pos())
add_board("test2")
print(find_open_rack_pos())
add_board("test3")
print(find_open_rack_pos())
print_rack()
remove_board("test")
print_rack()




