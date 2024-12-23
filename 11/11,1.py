data = open("C:\\Users\\bcher\\OneDrive\\Desktop\\programs\\advent2024\\gitHub\\Advent2024\\11\\in.txt").read()
data = data.split(" ")
for i in range(len(data)):
    data[i] = int(data[i])
numBlinks = 25

for i in range(numBlinks):
    stoneIndex = 0
    added = 0
    while stoneIndex+added < len(data):
        strStone = str(data[stoneIndex])
        if data[stoneIndex] == 0:
            data[stoneIndex] = 1
            stoneIndex = stoneIndex + 1
        elif len(strStone)%2==0:
            data.append(int(strStone[len(strStone)//2:]))
            data[stoneIndex] = int(strStone[0:len(strStone)//2:])
            stoneIndex = stoneIndex + 1
            added = added + 1
        else:
            data[stoneIndex] = data[stoneIndex]*2024
            stoneIndex = stoneIndex + 1

print(len(data))
