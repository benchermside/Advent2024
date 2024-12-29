data = open("C:\\Users\\bcher\\OneDrive\\Desktop\\programs\\advent2024\\gitHub\\Advent2024\\18\\in.txt").read()
data = data.split("\n")

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




obstructions = set()
for lineIndex in range(0, min(3010, len(data))):
    data[lineIndex] = data[lineIndex].split(",")
    data[lineIndex] = (int(data[lineIndex][0]), int(data[lineIndex][1]))
    obstructions.add(data[lineIndex])

print("data is", data[3011])

class situation:
    def __init__(self, cost, position):
        self.cost = cost
        self.position = position
    def __eq__(self, value):
        return self.position == value.position
    def __hash__(self):
        return hash(self.position)

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



# for rowIndex in range(len(map)):
#     for columIndex in range(len(map[0])):
#         if map[rowIndex][columIndex] == "S":
#             startPos = (rowIndex, columIndex)

myHeap = minHeap(getCost)
startPos = (0,0)

minLen = 0
maxLen = 70


myHeap.addElem(situation(0, startPos))
seenStates = {startPos}
finished = False
finalCost = None
while not finished:
    cheapestState = myHeap.popTop()
    cheapestStatePos = cheapestState.position
    for direction in [(1,0), (-1, 0), (0,1), (0,-1)]:
        nextPos = addTouples(cheapestStatePos, direction)
        if 0 <= nextPos[0] <= maxLen and 0 <= nextPos[1] <= maxLen and nextPos not in seenStates and nextPos not in obstructions:
            myHeap.addElem(situation(cheapestState.cost+1, nextPos))
            seenStates.add(nextPos)
            if nextPos == (maxLen, maxLen):
                finished = True
                finalCost = cheapestState.cost + 1
            


print(finalCost)
        
