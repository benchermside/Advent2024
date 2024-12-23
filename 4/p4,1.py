data = open("C:\\Users\\bcher\\OneDrive\\Desktop\\programs\\advent2024\\gitHub\\Advent2024\\4\\in.txt").read()
data = data.split("\n")

total = 0
for addSums in [[1, 0, 3, 0], [1, 1, 3, 3], [0, 1, 0, 3], [-1, 1, -3, 3]]:
    downDist = addSums[1]
    rightDist = addSums[0]
    downskip = addSums[3]
    rightSkip = addSums[2]
    skipFront = 0
    if rightSkip < 0:
        skipFront = -rightSkip
        rightSkip = 0
    for row in range(0, len(data)-downskip):
        for colum in range(skipFront, len(data[0])-rightSkip):
            currCheck = data[row][colum] + data[row+downDist][colum+rightDist] + data[row+downDist*2][colum+rightDist*2] + data[row+downDist*3][colum+rightDist*3]
            if currCheck == "XMAS" or currCheck == "SAMX":
                total = total + 1
print(total)
#print(2*total)
                