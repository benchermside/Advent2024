data = open("C:\\Users\\bcher\\OneDrive\\Desktop\\programs\\advent2024\\12\\in.txt").read()
data = data.split("\n")
countedPoints = set()


total = 0
for Y in range(len(data)):
    for X in range(len(data[Y])):
        if not (Y, X) in countedPoints:
            addedLastIttoration = {(Y,X)}
            addedThisIttoration = set()
            addedPreviusly = set()
            fencesList = []
            currSetType = data[Y][X]
            while len(addedLastIttoration) != 0:
                for newPoint in addedLastIttoration:
                    for vector in [(1,0), (0,1), (-1,0), (0,-1)]:
                        nextPoint = (newPoint[0]+vector[0], newPoint[1]+vector[1])
                        if -1 < nextPoint[0] < len(data) and -1 < nextPoint[1] < len(data[Y]) and nextPoint not in addedLastIttoration and nextPoint not in addedPreviusly and data[nextPoint[0]][nextPoint[1]] == currSetType:
                            addedThisIttoration.add(nextPoint)
                        else:
                            if nextPoint not in addedPreviusly and nextPoint not in addedLastIttoration:
                                fencesList.append((newPoint, vector))
                addedPreviusly.update(addedLastIttoration)
                addedLastIttoration = addedThisIttoration
                addedThisIttoration = set()
            discount = 0
            for fence1Index in range(len(fencesList)):
                fence1 = fencesList[fence1Index]
                for fence2Index in range(fence1Index+1, len(fencesList)):
                    fence2 = fencesList[fence2Index]
                    if fence1[1] == fence2[1]:
                        if (fence1[0][0]+fence1[1][1], fence1[0][1] + fence1[1][0]) == fence2[0] or (fence1[0][0]-fence1[1][1], fence1[0][1] - fence1[1][0]) == fence2[0]:
                            discount = discount + 1
            total = total + (len(fencesList)-discount)*len(addedPreviusly)
            countedPoints.update(addedPreviusly)
            
print(total)



