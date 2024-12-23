data = open("C:\\Users\\bcher\\OneDrive\\Desktop\\programs\\advent2024\\gitHub\\Advent2024\\12\\in.txt").read()
data = data.split("\n")
countedPoints = set()


total = 0
for Y in range(len(data)):
    for X in range(len(data[Y])):
        if not (Y, X) in countedPoints:
            addedLastIttoration = {(Y,X)}
            addedThisIttoration = set()
            addedPreviusly = set()
            currSetType = data[Y][X]
            numFences = 0
            while len(addedLastIttoration) != 0:
                for newPoint in addedLastIttoration:
                    for vector in [(1,0), (0,1), (-1,0), (0,-1)]:
                        nextPoint = (newPoint[0]+vector[0], newPoint[1]+vector[1])
                        if -1 < nextPoint[0] < len(data) and -1 < nextPoint[1] < len(data[Y]) and nextPoint not in addedLastIttoration and nextPoint not in addedPreviusly and data[nextPoint[0]][nextPoint[1]] == currSetType:
                            addedThisIttoration.add(nextPoint)
                        else:
                            if nextPoint not in addedPreviusly and nextPoint not in addedLastIttoration:
                                numFences = numFences + 1
                addedPreviusly.update(addedLastIttoration)
                addedLastIttoration = addedThisIttoration
                addedThisIttoration = set()
            total = total + numFences*len(addedPreviusly)
            countedPoints.update(addedPreviusly)
            
print(total)



