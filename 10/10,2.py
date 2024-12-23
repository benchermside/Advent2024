data = open("C:\\Users\\bcher\\OneDrive\\Desktop\\programs\\advent2024\\10\\in.txt").read()
data = data.split("\n")

def integMake(data):
    if data in "0123456789":
        return int(data)
    return -2

def getTrailHeadList(startRow, startColum, prevNum):
    if -1 < startRow < len(data) and -1 < startColum < len(data[0]):
        nextNum = data[startRow][startColum]
        if integMake(nextNum)-1 == integMake(prevNum):
            if nextNum == "9":
                return [(startColum, startRow)]
            else:
                destinations = []
                for vecotr in [(0,1), (0,-1), (1,0), (-1,0)]:
                    destinations = destinations + getTrailHeadList(startRow+vecotr[0], startColum+vecotr[1], nextNum)
                return destinations
                
        else:
            return []
    else:
        return []


total = 0
num0s = 0
for rowNum in range(len(data)):
    for columNum in range(len(data[rowNum])):
        if data[rowNum][columNum] == "0":
            num0s = num0s + 1
            destns = []
            destns = destns + getTrailHeadList(rowNum+1, columNum, "0")
            destns = destns + getTrailHeadList(rowNum-1, columNum, "0")
            destns = destns + getTrailHeadList(rowNum, columNum+1, "0")
            destns = destns + getTrailHeadList(rowNum, columNum-1, "0")
            total = total + len(destns)

print(total)