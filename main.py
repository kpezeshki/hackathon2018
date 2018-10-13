NUM_RACKS = 5

rack = [1]*NUM_RACKS


def lock_solenoid(num):
	pass
def unlock_solenoid(num):
	pass

class RackHolder:
	def __init__(self, position):
		self.isLocked = False
		self.position = position
		self.isClaimed = False
		self.studentIDNum = None

	def claim(self, id):
		
		self.isClaimed = True
		self.isLocked = True
		self.studentIDNum = id
		unlock_solenoid(self.position)

	def unclaim(self):
		self.isClaimed = False
		self.isLocked = False
		self.studentIDNum = None
		lock_solenoid(self.position)

	def __repr__(self):
		return "(P" + str(self.position) + " c:" + str(self.isClaimed) + " by " + str(self.studentIDNum) + ")"


racks = [RackHolder(i) for i in range(NUM_RACKS)]

def find_open_rack_pos():
	for rack in racks:
		if rack.isClaimed == False:
			return rack.position

def add_board(id):
	rack = racks[find_open_rack_pos()]
	rack.claim(id)
	print("rack", rack, "claimed")

def find_rack(id):
	for rack in racks:
		if rack.studentIDNum == id:
			return rack

def remove_board(id):
	rack = find_rack(id)
	rack.unclaim()
	print("rack", rack, "unclaimed")

def print_rack():
	for rack in racks:
		print(rack)

add_board("test")
print(find_open_rack_pos())
add_board("test2")
print(find_open_rack_pos())
add_board("test3")
print(find_open_rack_pos())
print_rack()
remove_board("test")
print_rack()




