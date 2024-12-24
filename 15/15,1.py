data = open("C:\\Users\\bcher\\OneDrive\\Desktop\\programs\\advent2024\\gitHub\\Advent2024\\15\\in.txt").read()
data = data.split("\n\n")
grid = data[0].split("\n")
moves = data[1].replace("\n", "")

for i in range(len(grid)):
    grid[i] = list(grid[i])


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
    destination = addTouples(moveVector, robotPos)
    moveCount = 1
    while grid[destination[0]][destination[1]] != "." and grid[destination[0]][destination[1]] != "#":
        destination = addTouples(destination, moveVector)
        moveCount = moveCount + 1
    if grid[destination[0]][destination[1]] == ".":
        reverseVector = multTouple(moveVector, -1)
        for moveIndex in range(moveCount):
            prevLocation = addTouples(destination, reverseVector)
            grid[destination[0]][destination[1]] = grid[prevLocation[0]][prevLocation[1]]
            destination = prevLocation
        grid[destination[0]][destination[1]] = "."
        robotPos = addTouples(robotPos, moveVector)

#printMap()
total = 0
for rowIndex in range(len(grid)):
    for columIndex in range(len(grid[rowIndex])):
        if grid[rowIndex][columIndex] == "O":
            total = total + 100*rowIndex + columIndex


print(total)


