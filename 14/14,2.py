import time
import sys
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

def showRobots(robotList, ittoration):
    feild = []
    for i in range(103):
        feild.append([])
        for j in range(101):
            feild[i].append(".")
    
    possibleTree = False
    for robot in robotList:
        feild[robot.Ypos][robot.Xpos] = "*"
        try:
            if  0 < robot.Ypos < 102 and 0 < robot.Xpos < 100:
                allFull = True
                for RowAdd in range(-1, 2):
                    for columAdd in range(-1, 2):
                        if feild[robot.Ypos+RowAdd][robot.Xpos+columAdd] == ".":
                            allFull = False
                if allFull:
                    possibleTree = True
        except IndexError:
            print("index error", robot.Ypos, robot.Xpos, RowAdd, columAdd)
            a = 1/0




    if possibleTree:
        for line in feild:
            for pos in line:
                print(pos, end="")
            print()
        print("itoration num", ittoration)
        print()
        print()
        time.sleep(1)
    
robots = []
for datum in data:
    robots.append(robot(datum))

start = 0

for i in range(10000):
    if start <= i:
        showRobots(robots, i)
    if i%100 == 0:
        print("compleated run", i)
    for currRobot in robots:
        currRobot.Move(1)

print("done")




