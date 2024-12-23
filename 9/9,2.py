data = open("C:\\Users\\bcher\\OneDrive\\Desktop\\programs\\advent2024\\9\\in.txt").read()

def sumIntervol(numL, numH):
    numL = numL - 1
    numH = numH - 1
    return ((numH*numH + numH)//2)-((numL*numL+numL)//2)


usedSpace = []
freeSpace = []
even = True
for char in data:
    if even:
        usedSpace.append(int(char))
    else:
        freeSpace.append([int(char)])
    even = not even

for i in range(len(usedSpace)-1,-1, -1):
    for j in range(i-1):
        if  freeSpace[j][0] >= usedSpace[i]:
            freeSpace[j].append([usedSpace[i], i])
            freeSpace[j][0] = freeSpace[j][0] - usedSpace[i]
            usedSpace[i] = None
            break
    
print(usedSpace)
print(freeSpace)


lowIndex = 0
#highIndex = len(data)-1
highIndexUsed = 0
currId = 0
total = 0



while(lowIndex < len(usedSpace)+len(freeSpace)):
    if lowIndex%2 == 0:
        currCorrospIndex = lowIndex//2
        if usedSpace[currCorrospIndex] != None:
            total = total + (lowIndex//2)*sumIntervol(currId, currId + int(usedSpace[currCorrospIndex]))
            currId = currId + int(usedSpace[currCorrospIndex])
    else:
        currCorrospIndex = (lowIndex-1)//2
        for i in range(1, len(freeSpace[currCorrospIndex])):
            currLine = freeSpace[currCorrospIndex][i]
            total = total + (currLine[1])*sumIntervol(currId, currId + int(currLine[0]))
            currId = currId + int(currLine[0])
        currId = currId + freeSpace[currCorrospIndex][0]



    lowIndex = lowIndex + 1
    print(total)

# if highIndex == lowIndex and lowIndex%2==0:
#     print("entered")
#     while highIndexUsed<int(data[highIndex]):
#         total = total + currId*(lowIndex//2)
#         currId = currId + 1
#         highIndexUsed = highIndexUsed + 1
# else:
#     print(highIndexUsed)
#     print(lowIndex)
#     print(highIndex)




print(total)