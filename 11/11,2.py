data = open("C:\\Users\\bcher\\OneDrive\\Desktop\\programs\\advent2024\\11\\in.txt").read()
data = data.split(" ")
rockClasifications = {}
for i in range(len(data)):
    rockClasifications[int(data[i])] = 1
numBlinks = 75

for i in range(numBlinks):
    nextRockClasifications = {}
    for classification in rockClasifications:
        strStone = str(classification)
        if classification == 0:
            numCurrRocks = nextRockClasifications.get(1)
            if numCurrRocks == None: 
                nextRockClasifications[1] = rockClasifications[classification]
            else:
                nextRockClasifications[1] = numCurrRocks + rockClasifications[classification]
        elif len(strStone)%2==0:
            toAdd1 = strStone[0:len(strStone)//2]
            toAdd2 = strStone[len(strStone)//2:]
            for toAdd in [toAdd1, toAdd2]:
                toAddInt = int(toAdd)
                numCurrRocks = nextRockClasifications.get(toAddInt)
                if numCurrRocks == None:
                    nextRockClasifications[toAddInt] = rockClasifications[classification]
                else:
                    nextRockClasifications[toAddInt] = numCurrRocks + rockClasifications[classification]
        else:
            numCurrRocks = nextRockClasifications.get(classification*2024, 0)
            nextRockClasifications[classification*2024] = numCurrRocks + rockClasifications[classification]
    rockClasifications = nextRockClasifications
    
total = 0
for rock in rockClasifications:
    total = total + rockClasifications[rock]
print(total)