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


for Y in range(len(map)):
    for X in range(len(map)):
        if map[Y][X] == "S":
            strartPos = (Y,X)
            map[Y] = map[Y][0:X] + "." + map[Y][X+1:]
        if map[Y][X] == "E":
            endPos = (Y,X)
            map[Y] = map[Y][0:X] + "." + map[Y][X+1:]

unitVectors = [(1,0), (-1,0),(0,1), (0,-1)]
posDistences = {}
currPos = strartPos
distFromStart = 0
while currPos not in posDistences:
    posDistences[currPos] = dist(distFromStart, None)
    for vector in unitVectors:
        nextPos = addTouples(currPos, vector)
        if nextPos not in posDistences and -1 < nextPos[0] < len(map) and -1 < nextPos[1] < len(map[0]) and map[nextPos[0]][nextPos[1]] == "." :
            currPos = nextPos
            distFromStart = distFromStart + 1
            break


maxDist = distFromStart
minCheat = 100


skips = []
for Y in range(len(map)):
    for X in range(len(map[0])):
        currVal = map[Y][X]
        if currVal == "#":
            checkingPos = (Y, X)
            for V1Index in range(4):
                for V2Index in range(V1Index+1, 4):
                    V1 = unitVectors[V1Index]
                    V2 = unitVectors[V2Index]
                    Pos1 = addTouples(V1, checkingPos)
                    Pos2 = addTouples(V2, checkingPos)
                    if -1 < Pos1[0] < len(map) and -1 < Pos1[1] < len(map[0]) and -1 < Pos1[0] < len(map) and -1 < Pos2[1] < len(map[0]):
                        if map[Pos1[0]][Pos1[1]] == "." and map[Pos2[0]][Pos2[1]] == ".":
                            if abs(posDistences[Pos1].start - posDistences[Pos2].start)-2 >= minCheat:
                                skips.append((Pos1, Pos2))

print(len(skips))

        


