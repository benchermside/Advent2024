data = open("C:\\Users\\bcher\\OneDrive\\Desktop\\programs\\advent2024\\gitHub\\Advent2024\\7\\in.txt").read()
data = data.split("\n")

for i in range(len(data)):
    data[i] = data[i].split(": ")
    data[i][1] = data[i][1].split(" ")
    for j in range(len(data[i][1])):
        data[i][1][j] = int(data[i][1][j])
    data[i][0] = int(data[i][0])

total = 0

def applyOpp(total, addition, opp):
    if opp:
        return total + addition
    else:
        return total*addition

for line in data:
    numOpps = len(line[1])-1
    opperators = [True]*numOpps
    numLoops = 0
    lineWorks = False
    overFlowed = False
    while not overFlowed:
        currSetWorks = False
        currTotal = line[1][0]
        for oppNum in range(1, numOpps+1):
            currTotal = applyOpp(currTotal, line[1][oppNum], opperators[oppNum-1])
        if currTotal == line[0]:
            lineWorks = True
            break
        currOP = 0
        madeFalse = False
        # print("loop num", numLoops)
        # print("opperators is", opperators)
        while not madeFalse:
            if currOP<len(opperators):
                opperators[currOP] = not opperators[currOP]
                if opperators[currOP] == False:
                    madeFalse = True
            else:
                overFlowed = True
                madeFalse = True
            currOP = currOP + 1
        numLoops = numLoops + 1
    if lineWorks:
        total = total + line[0]
        print("works")
    else:
        print("does not work")
    
    # print("line end")
    # print()

print(total)
    
