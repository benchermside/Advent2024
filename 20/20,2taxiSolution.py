data = open("C:\\Users\\bcher\\OneDrive\\Desktop\\programs\\advent2024\\gitHub\\Advent2024\\20\\in.txt").read()
map = data.split("\n")

print()
class dist:
    def __init__(self, start, end):
        self.start = start
        self.end = end

def onMap(pos):
    return -1 < pos[0] < len(map) and -1 < pos[1] < len(map[0])


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

def getTaxyDist(pos1, pos2):
    return abs(pos1[0]-pos2[0])+abs(pos1[1]-pos2[1])


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
    posDistences[currPos] = distFromStart
    for vector in unitVectors:
        nextPos = addTouples(currPos, vector)
        if nextPos not in posDistences and -1 < nextPos[0] < len(map) and -1 < nextPos[1] < len(map[0]) and map[nextPos[0]][nextPos[1]] == "." :
            currPos = nextPos
            distFromStart = distFromStart + 1
            break


maxDist = distFromStart
minCheat = 100

total = 0
skips = []
for Y1 in range(len(map)):
    for X1 in range(len(map[0])):
        currVal1 = map[Y1][X1]
        if currVal1 != "#":
            for Y2 in range(Y1-20, Y1+21):
                for X2 in range(X1-20, X1+21):
                    taxyDist = getTaxyDist((Y1, X1), (Y2, X2))
                    if onMap((Y2, X2)) and taxyDist <= 20:
                        currVal2 = map[Y2][X2]
                        if currVal2 != "#":
                            dist1 = posDistences[(Y1, X1)]
                            dist2 = posDistences[(Y2, X2)]
                            if dist1 - dist2 >= minCheat+taxyDist:
                                total = total + 1



            # checkingPos = (Y, X)
            # for V1Index in range(4):
            #     for V2Index in range(V1Index+1, 4):
            #         V1 = unitVectors[V1Index]
            #         V2 = unitVectors[V2Index]
            #         Pos1 = addTouples(V1, checkingPos)
            #         Pos2 = addTouples(V2, checkingPos)
            #         if -1 < Pos1[0] < len(map) and -1 < Pos1[1] < len(map[0]) and -1 < Pos1[0] < len(map) and -1 < Pos2[1] < len(map[0]):
            #             if map[Pos1[0]][Pos1[1]] == "." and map[Pos2[0]][Pos2[1]] == ".":
            #                 if abs(posDistences[Pos1].start - posDistences[Pos2].start)-2 >= minCheat:
            #                     skips.append((Pos1, Pos2))

print(total)

        


