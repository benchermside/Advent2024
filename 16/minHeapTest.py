import random

class situation:
    def __init__(self, cost, position, direction):
        self.cost = cost
        self.position = position
        self.direction = direction

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
        
myHeap = minHeap()
for i in range(5000):
    myHeap.addElem(random.randint(0, 10000))
sortedList = []
for i in range(5000):
    sortedList.append(myHeap.popTop())
print(sortedList)