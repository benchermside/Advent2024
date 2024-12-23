data = open("C:\\Users\\bcher\\OneDrive\\Desktop\\programs\\advent2024\\gitHub\\Advent2024\\8\\in.txt").read()
data = data.split("\n")

gridLen = len(data[0])
gridHeight = len(data)
antenaList = {}
for y in range(gridHeight):
    for x in range(gridLen):
        curr = data[y][x]
        if curr != ".":
            if antenaList.get(curr) == None:
                antenaList[curr] = [(y, x)]
            else:
                antenaList[curr].append((y,x))
recSet = set()

for towerType in antenaList:
    towerList = antenaList[towerType]
    for i in range(len(towerList)):
        for j in range(i+1, len(towerList)):
            tower1 = towerList[i]
            tower2 = towerList[j]
            xdif = tower1[1] - tower2[1]
            ydif = tower1[0] - tower2[0]
            foundBelow = []
            foundAbove = []
            nextFind = tower1
            while -1<nextFind[0]<gridHeight and -1<nextFind[1]<gridHeight:
                foundBelow.append(nextFind)
                nextFind = (nextFind[0] - ydif, nextFind[1] - xdif)
            nextFind = (tower1[0]+ydif, tower1[1]+xdif)
            while -1<nextFind[0]<gridHeight and -1<nextFind[1]<gridHeight:
                foundAbove.append(nextFind)
                nextFind = (nextFind[0] + ydif, nextFind[1] + xdif)
            for find in foundAbove:
                recSet.add(find)
            for find in foundBelow:
                recSet.add(find)
            


print(len(recSet))
