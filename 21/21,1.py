data = open("C:\\Users\\bcher\\OneDrive\\Desktop\\programs\\advent2024\\gitHub\\Advent2024\\21\\in.txt").read()
Codes = data.split("\n")


class robot:
    def __init__(self, bord, bordNone, pos, masterRobot=None):
        self.bord = bord#the bord that the thing is on, includes None where empty, index from self.board[Y][X]
        self.bordNone = bordNone#the cowardinents of the None space on self.bord
        self.pos = pos#your current position
        self.masterRobot = masterRobot#the robot you are being controlled by


bottomBord = [
    ["7","8","9"],
    ["4","5","6"],
    ["1","2","3"],
    [None, "0", "A"]
]
bottomBordNone = (3, 0)

middleBord = [
    [None, "^", "A"],
    ["<", "v", ">"]
]
middleBordNone = (0,0)

topRobot = robot(middleBord, middleBordNone, (0, 2), None)
secondRobot = robot(middleBord, middleBordNone, (0, 2), topRobot)
thirdRobot = robot(bottomBord, bottomBordNone, (3, 2), secondRobot)

def findKeyLocation(grid, key):
    for rowNum in range(len(grid)):
        for columNum in range(len(grid[0])):
            if grid[rowNum][columNum] == key:
                return (rowNum, columNum)
    print("keyNotFoundError")

def calculateVal(robot, key):
    if robot is None:
        return 1
    keyLocation = findKeyLocation(robot.bord)
    if (robot.pos[0]==robot.bordNone[0] or keyLocation[0]==robot.bordNone[0]) and (robot.pos[1]==robot.bordNone[1] or keyLocation[1]==robot.bordNone[1]):
        pass
    else:
        if robot.pos[0] < keyLocation[0]:
            key1 = "v"
        else:
            key1 = "^"
        if robot.pos[1] < keyLocation[1]:
            key2 = ">"
        else:
            key2 = "<"
        val1 = 0
        tempPosSave = robot.masterRobot.Pos
        for i in range(abs(robot.pos[0] - keyLocation[0])):
            val1 = val1 + calculateVal(robot.masterRobot, key1)
        for j in range(abs(robot.pos[1] - keyLocation[1])):
            val1 = val1 + calculateVal(robot.masterRobot, key2)
        val1 = val1 + calculateVal(robot.masterRobot, "A")
        robot.masterRobor.Pos = tempPosSave
        val2 = 0
        for i in range(abs(robot.pos[1] - keyLocation[1])):
            val1 = val1 + calculateVal(robot.masterRobot, key2)
        for j in range(abs(robot.pos[0] - keyLocation[0])):
            val1 = val1 + calculateVal(robot.masterRobot, key1)
        val2 = val2 + calculateVal(robot.masterRobot, "A")
        return min(val1, val2)

    

