# C:\ProgramData\Anaconda3\Scripts\ipython3.exe
# C:\Users\Nathan\hackathon2018


import time, random
from gpiozero import LED, Button

solenoid = LED(4)
limit_switch = Button(17)

limit_switch_status = 0
def limit_switch_on():
	limit_switch_status = 1

def limit_switch_off():
	limit_switch_status = 0


limit_switch.when_pressed = limit_switch_on.on
limit_switch.when_released = led.limit_switch_off

RACK_SIZE = 5
FILE_NAME = "Rack_Status.txt"

lockIDs = {} #lockIDs keeps a record of which position in the rack a given id has reserved
racklots = [] #racklots keeps a record of which slots in the rack are empty and full

class Slot:

	def __init__(self, position):
		self.isLocked = False
		self.position = position
		self.isClaimed = False
		self.studentIDNum = None
		#self.hasBoard = False
		#self.isHingeOpen = False

	def claim(self, studentID):

		#unlocks the solenoid
		unlock_solenoid(self.position)

		#waits while the user opens the rack and inserts the board
		while isHingeOpen(self.position) == False:
			time.sleep(0.1)

		#once the rack is re-closed, the states will update
		self.isClaimed = True
		self.isLocked = True
		self.studentIDNum = studentID
		lock_solenoid(self.position)

	def unclaim(self):

		#unlocks the solenoid
		unlock_solenoid(self.position)

		#waits for the user to open the door
		while isHingeOpen(self.position) == False:
			time.sleep(0.1)

		#once the rack is re-closed, the states will update
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

rack = [Slot(i) for i in range(RACK_SIZE)]

def find_open_slot_pos():
	for slot in rack:
		if slot.isClaimed == False:
			return slot.position

def add_board(studentID):
	slot = rack[find_open_slot_pos()]
	slot.claim(studentID)

def find_slot(studentID):
	for slot in rack:
		if slot.studentIDNum == studentID:
			return slot.position

def remove_board(studentID):
	slot = rack[find_slot(studentID)]
	slot.unclaim()

def add_remove_board(studentID):
	# checks that the input is a number
	try:
		studentID = int(studentID)
		studentID = str(studentID)
		if find_slot(studentID) != None:
			remove_board(studentID)
		else:
			add_board(studentID)
	except:
		return

def print_rack():
	output = ""
	for slot in rack:
		output += str(slot) + "\n"
	return output


def isHingeOpen(position):
	return limit_switch_status
	"""
	limitSwitchInput = random.getrandbits(1)	 
	if (limitSwitchInput > 0): #on
		return True
	else: #off
		False"""

def lock_solenoid(num):
	solenoid.off()

def unlock_solenoid(num):
	solenoid.on()

def hasBoard(ultrasonicSensorInput):
	pass

def main():
	while True:
		studentID = input()
		add_remove_board(studentID)
		print(print_rack())
		f = open(FILE_NAME, 'w')
		f.write(print_rack())
		f.close()
		
if __name__ == "__main__":
	main()
