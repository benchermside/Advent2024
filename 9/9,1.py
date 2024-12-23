data = open("C:\\Users\\bcher\\OneDrive\\Desktop\\programs\\advent2024\\9\\in.txt").read()

def sumIntervol(numL, numH):
    numL = numL - 1
    numH = numH - 1
    return ((numH*numH + numH)//2)-((numL*numL+numL)//2)
    


lowIndex = 0
highIndex = len(data)-1
highIndexUsed = 0
currId = 0
total = 0

while(lowIndex < highIndex):
    if lowIndex%2 == 0:
        total = total + (lowIndex//2)*sumIntervol(currId, currId + int(data[lowIndex]))
        currId = currId + int(data[lowIndex])
    elif highIndex<1:
        pass
    else:
        j = 0
        while j<int(data[lowIndex]):   
            if highIndex%2 == 0 and highIndexUsed<int(data[highIndex]) and lowIndex<highIndex:
                total = total + (highIndex//2)*currId
                currId = currId + 1
                highIndexUsed = highIndexUsed + 1
                j = j+1
            elif highIndex%2 == 1:
                highIndex = highIndex - 1
                highIndexUsed = 0
            elif highIndexUsed >= int(data[highIndex]):
                highIndex = highIndex - 2
                highIndexUsed = 0
            else:
                print("impossable state reached")
                j = j +1

    lowIndex = lowIndex + 1

if highIndex == lowIndex and lowIndex%2==0:
    print("entered")
    while highIndexUsed<int(data[highIndex]):
        total = total + currId*(lowIndex//2)
        currId = currId + 1
        highIndexUsed = highIndexUsed + 1
else:
    print(highIndexUsed)
    print(lowIndex)
    print(highIndex)




print(total)