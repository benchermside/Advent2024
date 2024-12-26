data = open("C:\\Users\\bcher\\OneDrive\\Desktop\\programs\\advent2024\\gitHub\\Advent2024\\15\\in.txt").read()
data = data.split("\n\n")
grid = data[0].split("\n")
moves = data[1].replace("\n", "")

for i in range(len(grid)):
    newLine = []
    for elem in grid[i]:
        if elem == "#":
            newLine.append("#")
            newLine.append("#")
        elif elem == "O":
            newLine.append("[")
            newLine.append("]")
        elif elem == ".":
            newLine.append(".")
            newLine.append(".")
        elif elem == "@":
            newLine.append("@")
            newLine.append(".")
        else:
            print("imposable state reached")
    grid[i] = newLine


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

def printMap():
    for row in grid:
        for colum in row:
            print(colum, end="")
        print()
    print()


for Y in range(len(grid)):
    for X in range(len(grid[0])):
        if grid[Y][X] == "@":
            robotPos = (Y, X)

GetVector = {"<": (0, -1), ">":(0,1), "^":(-1,0),"v":(1,0)}
for move in moves:
    moveVector = GetVector[move]
    firstDest = addTouples(moveVector, robotPos)
    MovedIntoLevelPoints = [set(),{firstDest}]
    rowsPassed = 1
    noWalls = grid[firstDest[0]][firstDest[1]] != "#"
    anyBoxes = grid[firstDest[0]][firstDest[1]] in ["[","]"]
    while noWalls and anyBoxes:
        noWalls = True
        anyBoxes = False
        MovedIntoLevelPoints.append(set())
        for destination in MovedIntoLevelPoints[rowsPassed]:
            destinationContents = grid[destination[0]][destination[1]]
            if destinationContents == "#":
                noWalls = False
            elif destinationContents in ["[","]"]:
                anyBoxes = True
                MovedIntoLevelPoints[rowsPassed+1].add(addTouples(destination, moveVector))
                if moveVector[1] == 0:
                    if destinationContents == "[":
                        otherBoxLocation = addTouples(destination, (0, 1))
                    elif destinationContents == "]":
                        otherBoxLocation = addTouples(destination, (0, -1))
                    else:
                        print("https://www.xkcd.com/2200")
                    MovedIntoLevelPoints[rowsPassed+1].add(addTouples(otherBoxLocation, moveVector))
        rowsPassed = rowsPassed + 1
    if noWalls:
        inversMoveVector = multTouple(moveVector, -1)
        for MovedIntoRowIndex in range(len(MovedIntoLevelPoints)-1, -1, -1):
            MovedIntoRow = MovedIntoLevelPoints[MovedIntoRowIndex]
            for movedInto in MovedIntoRow:
                moveFrom = addTouples(inversMoveVector, movedInto)
                if grid[moveFrom[0]][moveFrom[1]] == "@":
                    robotPos = movedInto
                grid[movedInto[0]][movedInto[1]] = grid[moveFrom[0]][moveFrom[1]]
                grid[moveFrom[0]][moveFrom[1]] = "."



printMap()
total = 0
for rowIndex in range(len(grid)):
    for columIndex in range(len(grid[rowIndex])):
        if grid[rowIndex][columIndex] == "[":
            total = total + 100*rowIndex + columIndex


print(total)


