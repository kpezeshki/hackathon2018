# MuddHacks 2018 Card Reader Code

# C:\ProgramData\Anaconda3\Scripts\ipython3.exe
# C:\Users\Nathan\hackathon2018

lockIDs = {}
rackSlots = []
 

def initializeRack(slots):
    '''
    Makes a new rack with a number of slots slots
    '''
    for i in range(slots-1):
        rackSlots.append(0)
    print(rackSlots)

def addBoard(studentID):
    '''
    Adds a board to the rack in the first available position registered under the entered ID
    Sets the status of that rack position as full (1) 
    Creates a new entry in the lockIDs dictionary to log which rack position corresponds to the studentID
    @param studentID a string representation of the studentID number
    ''' 
    for i in range(len(rackSlots)-1):
        if rackSlots[i] == 0 and not(studentID in lockIDs):
            lockIDs[str(studentID)] = i
            rackSlots[i] = 1
            #Lock Open/Close
            break
        #else:
            #do other thing
    print(rackSlots)


def removeBoard(studentID):
    '''
    Opens the lock to which the studentID is registered
    Removes the studentID from the list of IDs currently registered to the lock
    @param studentID a string representation of the studentID number
    '''
    rackSlots[lockIDs[studentID]] = 0
    del lockIDs[studentID]
    print(rackSlots)
    #Lock Open/Close

def addRemoveBoard(studentID):
    try: 
        studentID = int(studentID)
        studentID = str(studentID)
        if studentID in lockIDs:
            removeBoard(studentID)
        else:
            addBoard(studentID)
    except:
        return

def acceptInput():
    """
    Scanner to continuously accept input of studentIDs
    """
    while True:
        studentID = input("Enter your input: ")
        addRemoveBoard(studentID)


initializeRack(10)
acceptInput()




