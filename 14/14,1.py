data = open("C:\\Users\\bcher\\OneDrive\\Desktop\\programs\\advent2024\\14\\in.txt").read()
data = data.split("\n")
for i in range(len(data)):
    data[i] = data[i].split(" ")
    data[i][0] = data[i][0].split(",")
    data[i][1] = data[i][1].split(",")

class robot:
    def __init__(self, infoList):
        self.Xpos = int(infoList[0][0][2:])
        self.Ypos = int(infoList[0][1])
        self.Xvelocity = int(infoList[1][0][2:])
        self.Yvelocity = int(infoList[1][1])
    def Move(self, dist):
        self.Xpos = (self.Xpos + dist*self.Xvelocity)%101
        self.Ypos = (self.Ypos + dist*self.Yvelocity)%103

robots = []
for datum in data:
    robots.append(robot(datum))

Quad1 = 0
Quad2 = 0
Quad3 = 0
Quad4 = 0


for currRobot in robots:
    currRobot.Move(100)
    if currRobot.Xpos < 50:
        if currRobot.Ypos < 51:
            Quad1 = Quad1 + 1
        elif currRobot.Ypos > 51:
            Quad2 = Quad2 + 1
    elif currRobot.Xpos > 50:
        if currRobot.Ypos < 51:
            Quad3 = Quad3 + 1
        elif currRobot.Ypos > 51:
            Quad4 = Quad4 + 1

print(Quad1*Quad2*Quad3*Quad4)


