"""
There are 1000 doors in a high school with 1000 students. 
The problem begins with the first student opening all 1000 doors.
next the second student closes doors 2,4,6,8,10 and so on to door 
1000 the third student changes the state (opens doors closed, closes doors s open)
on doors 3,6,9,12,15 and so on the fourth student Changes the state of doors 4, 8, 12, 16 and so on.
This goes on until every student has had a turn. How many doors will be open at the end?
"""

#For any number of people in circle using only Python list and for loop

DoorList = ["Index Adjustment dummy element"]                         #First element to occupy index 0
DoorNos = int(input("Total number of Closed doors at start = "))

for x in range(0,DoorNos):                                            #Making a list where all elements are "C" representing closed doors
    DoorList.append("C")
  
for x in range(2,len(DoorList),2):                                    #Number 2's turn who turns "C" doors to "O" opened ones
    DoorList[x] = "O"
  
for i in range(3,len(DoorList)):                                      #Doing iterations from 3 to all doors
    for x in range(i,len(DoorList),i):
        if DoorList[x] == "O":
            DoorList[x] = "C"
        else:
            DoorList[x] = "O"
         
OpenedDoors = 0

for x in DoorList:                                                     #Counting all opened doors
    if x == "C":
        OpenedDoors = OpenedDoors + 1
    
print("Total number of Opened Doors in the end = ", OpenedDoors)
indices = [i for i, x in enumerate(DoorList) if x == "C"]              #Adding idices of all opened doors in the end

print("Door nos. in opened position in th end =", indices)


