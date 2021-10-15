import time
callButtonID = 1

# ******     THE OBJECT FUNCTION THAT CREATES THE COLUMNS     ******
class Column:
    def __init__(self, _id, _amountOfFloors, _amountOfElevators):
        self.ID = _id
        self.amountOfFloors = _amountOfFloors
        self.status = "idle"
        self.amountOfElevators = _amountOfElevators
        self.elevatorList = []
        self.callButtonList = []
        for i in range(self.amountOfElevators):
            self.elevatorList.append(Elevator(i + 1,self.amountOfFloors))
        self.createCallButtons()
    # FUNCTION WITH A FOR LOOP TO CREATE 18 BUTTONS
    def createCallButtons(self):
        global callButtonID
        buttonFloor = 1
        for i in range(self.amountOfFloors):
            if buttonFloor < self.amountOfFloors:
                self.callButtonList.append(CallButton(i,buttonFloor,'up'))
                callButtonID += 1
            if buttonFloor > 1:

                 self.callButtonList.append(CallButton(i,buttonFloor,'down'))
                 callButtonID += 1
            buttonFloor = buttonFloor + 1
        
    # FUNCTION THAT FINDS THE NEAREST ELEVATOR AND RETURN IT'S ID
    def findElevator(self,floor,direction):
        selectableElevator = []
        numbers = []

        for i in range(len(self.elevatorList)):
                if self.elevatorList[i].status == "idle":
                    selectableElevator.append(self.elevatorList[i].ID)
                elif self.elevatorList[i].direction == 'up' and direction == 'up':

                    selectableElevator.append(self.elevatorList[i].ID)
                elif self.elevatorList[i].direction == 'down' and direction == 'down':

                    selectableElevator.append(self.elevatorList[i].ID)
        # LIST OF THE SELECATABLE ELEVATORS THAT COULD BE USED
        # MATH FUNCTION THAT RETURNS FIND THE CLOSEST ELEVATOR AND RETURN ITS ID
        for i in range(len(selectableElevator)):
            numbers.append(floor - self.elevatorList[i].currentFloor)
     
        return numbers.index(numbers[min(range(len(numbers)), key = lambda i: abs(numbers[i]-0))])

    # FUNCTION THAT HANDLE THE ELEVATOR REQUEST: FIND THE BEST ELEVATOR, ADD THE FLOOR TO REQUEST LIST, CALL TO MOVE AND OPERATE DOORS
    
    def requestElevator(self,floor,direction):
        elevator = self.findElevator(floor,direction)
        print(elevator)
        self.elevatorList[elevator].floorRequestList.append(floor)
        self.elevatorList[elevator].move()
        self.elevatorList[elevator].operateDoors

        return self.elevatorList[elevator]


# ******     THE FUNCTION THAT CREATES THE ELEVATORS AND HANDLES THEMS     ******

class Elevator:
    def __init__(self, _id, _amountOfFloors):
        self.ID = _id
        self.amountOfFloors = _amountOfFloors
        self.status = "idle"
        self.direction = ""
        self.door = Door(0)
        self.currentFloor = 1
        self.floorRequestButtonList = []
        self.floorRequestList = []
        # FUNCTION THAT CREATES THE BUTTON INSIDE THE ELEVATOR
      
        for i in range(self.amountOfFloors):
            self.floorRequestButtonList.append(FloorRequestButton(i,i))

    
    
    # FUNCTION THAT GETS THE DESTINATION FLOOR AND ADD IT TO THE QUEUE
    
    def requestFloor(self,floor):
        self.floorRequestList.append(floor)
        self.move()

    # FUNCTION THAT MAKES THE SELECTED ELEVATOR MOVE TO THE DESTINATION
    def move(self):
        while self.floorRequestList:
            destination = self.floorRequestList[0]
            self.status = "MOVING"

            if self.currentFloor < destination:
                self.direction = 'up'
                self.sortFloorList()
                while self.currentFloor < destination:
                    self.currentFloor = self.currentFloor + 1
            elif    self.currentFloor > destination:
                self.direction = 'down'
                self.sortFloorList()
                while self.currentFloor > destination:
                    self.currentFloor = self.currentFloor - 1
            self.status = "STOPPED"
            self.floorRequestList.pop(0)

        self.status = 'idle'


    #  FUNCTION THAT SORT THE QUEUE LIST IN ORDER OF THE DIRECTION
     
    def sortFloorList(self):
        if self.direction == 'up':
            self.floorRequestList.sort()
        elif self.direction == 'down':
            self.floorRequestList.sort(reverse = True)
    # FUNCTION THAT OPERATES THE DOOR : CLOSE OR OPEN IT
    def operateDoors(self):

        if(self.door.status == 'OPEND'):
            time.sleep(5)
            self.door.status == 'CLOSED'
        elif self.door.status== 'CLOSED' :
            time.sleep(5)
            self.door.status == 'OPEN'




#          ******     THE FUNCTION THAT CREATES THE EXTERIOR BUTTONS(OUTSIDE ELEVATORS)     ******
class CallButton:
    def __init__(self, _id, _floor, _direction):
        self.ID = _id
        self.floor = _floor
        self.direction = _direction
        self.status = 'on'

#          ******     THE FUNCTION THAT CREATES THE INTERIOR BUTTONS(INSIDE ELEVATORS)   ******
class FloorRequestButton:
    def __init__(self, _id, _floor):
        self.ID = _id
        self.floor = _floor
        self.status = 'on'
#          ******     THE FUNCTION THAT CREATES THE DOORS     ******
class Door:
    def __init__(self, _id):
        self.ID = _id
        self.status = 'closed'