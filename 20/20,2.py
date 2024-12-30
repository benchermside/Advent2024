data = open("C:\\Users\\bcher\\OneDrive\\Desktop\\programs\\advent2024\\gitHub\\Advent2024\\20\\in.txt").read()
map = data.split("\n")

print()
class dist:
    def __init__(self, start, end):
        self.start = start
        self.end = end


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

def onMap(pos):
    return -1 < pos[0] < len(map) and -1 < pos[1] < len(map[0])

def removeDups(oldList):
    newSet = set()
    for elem in oldList:
        newSet.add(elem)
    return list(newSet)


for Y in range(len(map)):
    for X in range(len(map)):
        if map[Y][X] == "S":
            strartPos = (Y,X)
            map[Y] = map[Y][0:X] + "." + map[Y][X+1:]
        if map[Y][X] == "E":
            endPos = (Y,X)
            map[Y] = map[Y][0:X] + "." + map[Y][X+1:]

unitVectors = [(1,0), (-1,0),(0,1), (0,-1)]


posDistences = {strartPos:0}
distFromStart = 0
currPoses = [strartPos]
while endPos not in currPoses:
    newPoses = []
    for currPos in currPoses:
        for vector in unitVectors:
            nextPos = addTouples(currPos, vector)
            if nextPos not in posDistences and onMap(nextPos) and map[nextPos[0]][nextPos[1]] == ".":
                newPoses.append(nextPos)
                posDistences[nextPos] = distFromStart+1
    currPoses = newPoses
    distFromStart = distFromStart + 1

totalDist = distFromStart



#cheatStart = 0
cheated = True
bestTime = 9999999999999999
for cheatStart in range(0, totalDist):
    posDistences = {strartPos:0}
    distFromStart = 0
    currPoses = [strartPos]
    while distFromStart + 50<totalDist:
        if distFromStart == cheatStart:
            addedCheats = set()
            cheatList = []
            prevPart = [currPos]
            for cheatListIndex in range(19):
                cheatList.append([])
                for part in prevPart:
                    for vector in unitVectors:
                        nextDest = addTouples(vector, part)
                        if nextPos not in addedCheats and onMap(nextDest):
                            addedCheats.add(nextDest)
                            cheatList[cheatListIndex].append(nextDest)
                prevPart = cheatList[cheatListIndex]
        if cheatStart < distFromStart < cheatStart+20:
            currPoses = removeDups(currPoses + cheatList[distFromStart-cheatStart-1])
        newPoses = []
        for currPos in currPoses:
            for vector in unitVectors:
                nextPos = addTouples(currPos, vector)
                if nextPos not in posDistences and -1 < nextPos[0] < len(map) and -1 < nextPos[1] < len(map[0]) and map[nextPos[0]][nextPos[1]] == ".":
                    newPoses.append(nextPos)
                    posDistences[nextPos] = distFromStart+1
                
        currPoses = newPoses
        distFromStart = distFromStart + 1
    


maxDist = distFromStart
minCheat = 100


# skips = []
# for Y in range(len(map)):
#     for X in range(len(map[0])):
#         currVal = map[Y][X]
#         if currVal == "#":
#             checkingPos = (Y, X)
#             for V1Index in range(4):
#                 for V2Index in range(V1Index+1, 4):
#                     V1 = unitVectors[V1Index]
#                     V2 = unitVectors[V2Index]
#                     Pos1 = addTouples(V1, checkingPos)
#                     Pos2 = addTouples(V2, checkingPos)
#                     if -1 < Pos1[0] < len(map) and -1 < Pos1[1] < len(map[0]) and -1 < Pos1[0] < len(map) and -1 < Pos2[1] < len(map[0]):
#                         if map[Pos1[0]][Pos1[1]] == "." and map[Pos2[0]][Pos2[1]] == ".":
#                             if abs(posDistences[Pos1].start - posDistences[Pos2].start)-2 >= minCheat:
#                                 skips.append((Pos1, Pos2))

# print(len(skips))

        


