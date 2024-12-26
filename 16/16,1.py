data = open("C:\\Users\\bcher\\OneDrive\\Desktop\\programs\\advent2024\\gitHub\\Advent2024\\16\\in.txt").read()
map = data.split("\n")

class situation:
    def __init__(self, cost, position, direction):
        self.cost = cost
        self.position = position
        self.direction = direction
    def __eq__(self, value):
        return self.direction == value.direction and self.position == value.position
    def __hash__(self):
        return hash((self.direction, self.position))

def less(a, b):
    return a<b

def printSList(sList):
    i = 0
    for elem in sList:
        print("elem", i, "cost", elem.cost)
        i = i + 1


class minHeap:
    def __init__(self, getKey=int):
        self.data = []
        self.getKey = getKey
    def addElem(self, elem):
        self.data.append(elem)
        elemIndex = len(self.data)-1
        if elemIndex%2==0:
            elemParentIndex = (elemIndex-1)//2
        else:
            elemParentIndex = elemIndex//2
        while elemIndex != 0 and self.getKey(self.data[elemParentIndex]) > self.getKey(self.data[elemIndex]):
            temp = self.data[elemParentIndex]
            self.data[elemParentIndex] = self.data[elemIndex]
            self.data[elemIndex] = temp
            elemIndex = elemParentIndex
            if elemIndex%2==0:
                elemParentIndex = (elemIndex-1)//2
            else:
                elemParentIndex = elemIndex//2
    # def heapafy(self, pos):
    #     self.data[0]

    def popTop(self):
        if len(self.data) < 2:
            if len(self.data) == 1:
                return self.data.pop()
            else:
                print("tryed to pop empty heap")
                return None
        top = self.data[0]
        self.data[0] = self.data.pop()
        parentIndex = 0
        leftChildIndex = (parentIndex*2)+1
        rightChildIndex = (parentIndex+1)*2
        notLeaf = leftChildIndex<len(self.data)
        if rightChildIndex<len(self.data):
            notBalanced = self.getKey(self.data[leftChildIndex]) < self.getKey(self.data[parentIndex]) or self.getKey(self.data[rightChildIndex]) < self.getKey(self.data[parentIndex])
        elif leftChildIndex < len(self.data):
            notBalanced = self.getKey(self.data[leftChildIndex]) < self.getKey(self.data[parentIndex])
        else:
            notBalanced = False
        while notLeaf and notBalanced:
            if len(self.data) == rightChildIndex or self.getKey(self.data[leftChildIndex]) < self.getKey(self.data[rightChildIndex]):
                self.data[leftChildIndex], self.data[parentIndex] = self.data[parentIndex], self.data[leftChildIndex]
                parentIndex = leftChildIndex
            else:
                self.data[rightChildIndex], self.data[parentIndex] = self.data[parentIndex], self.data[rightChildIndex]
                parentIndex = rightChildIndex
            leftChildIndex = (parentIndex*2)+1
            rightChildIndex = (parentIndex+1)*2
            notLeaf = leftChildIndex<len(self.data)
            if rightChildIndex < len(self.data):
                notBalanced = self.getKey(self.data[leftChildIndex]) < self.getKey(self.data[parentIndex]) or self.getKey(self.data[rightChildIndex]) < self.getKey(self.data[parentIndex])
            elif leftChildIndex < len(self.data):
                notBalanced = self.getKey(self.data[leftChildIndex]) < self.getKey(self.data[parentIndex])
            elif notLeaf:
                print("impossable state reached in popTop left child is", leftChildIndex, "right child is", rightChildIndex, "data size is", len(self.data))
        return top  
            



        
    
def getCost(state):
    return state.cost

def addTouples(touple1, touple2):
    list = []
    for elem in range(len(touple1)):
        list.append(touple1[elem]+touple2[elem])
    return tuple(list)

def multTouple(touple, int):
    list = []
    for elem in touple:
        list.append(elem*int)
    return tuple(list)


for rowIndex in range(len(map)):
    for columIndex in range(len(map[0])):
        if map[rowIndex][columIndex] == "S":
            startPos = (rowIndex, columIndex)

myHeap = minHeap(getCost)




rotate2 = {(-1,0):(0,1),(0,1):(1,0),(1,0):(0,-1),(0,-1):(-1,0)}
rotate3 = {(-1,0):(0,-1),(0,-1):(1,0),(1,0):(0,1),(0,1):(-1,0)}

startDirection = (0,1)
#StateList = [situation(0, startPos, startDirection)]
myHeap.addElem(situation(0, startPos, startDirection))
myHeap.addElem(situation(2000, startPos, multTouple(startDirection, -1)))
seenStates = {situation(0, startPos, startDirection), situation(2000, startPos, multTouple(startDirection, -1))}
finished = False
while not finished:
    # cheapestState = StateList[-1]
    # StateList.pop()
    cheapestState = myHeap.popTop()
    #print(cheapestState.cost)
    cheapestStatePos = cheapestState.position
    rotate2Direction = rotate2[cheapestState.direction]
    rotate2NextPos = addTouples(rotate2Direction,  cheapestStatePos)
    if map[rotate2NextPos[0]][rotate2NextPos[1]] != "#":
        newState2 = situation(cheapestState.cost + 1000, cheapestStatePos, rotate2Direction)
        if newState2 not in seenStates:
            myHeap.addElem(newState2)
            seenStates.add(newState2)
    rotate3Direction = rotate3[cheapestState.direction]
    rotate3NextPos = addTouples(rotate3Direction, cheapestStatePos)
    if map[rotate3NextPos[0]][rotate3NextPos[1]] != "#":
        newState3 = situation(cheapestState.cost + 1000, cheapestStatePos, rotate3Direction)
        if newState3 not in seenStates:
            myHeap.addElem(newState3)
            seenStates.add(newState3)
    nextPos = addTouples(cheapestStatePos, cheapestState.direction)
    if map[nextPos[0]][nextPos[1]] != "#":
        newState1 = situation(cheapestState.cost+1, nextPos, cheapestState.direction)
        if newState1 not in seenStates:
            if map[nextPos[0]][nextPos[1]] == "E":
                finished = True
                finalCost = newState1.cost
            seenStates.add(newState1)
            myHeap.addElem(newState1)
print(finalCost)
        
