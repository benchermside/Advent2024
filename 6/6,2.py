data = open("C:\\Users\\bcher\\OneDrive\\Desktop\\programs\\advent2024\\6\\in.txt").read()
data = data.split("\n")
for i in range(len(data)):
    data[i] = list(data[i])

#gaurdPosition = [None, None]
for y in range(len(data)):
    for x in range(len(data[y])):
        if data[y][x] == "^":
            #gaurdPosition = (y, x)
            gaurdStartPosition = (y, x)
            gaurdStartDirection = (-1, 0)
            data[y][x] = "."
gaurdDirectionRotation = {(-1,0):(0,1), (0,1):(1,0), (1,0):(0,-1), (0,-1):(-1,0)}
mapLen = len(data[0])
mapHeight = len(data)
total = 0

for yExtra in range(mapHeight):
    for xExtra in range(mapLen):
        if data[yExtra][xExtra] == "." and not gaurdStartPosition == (yExtra, xExtra):
            data[yExtra][xExtra] = "#"
            gaurdPosition = gaurdStartPosition
            gaurdDirection = gaurdStartDirection
            seenStates = {(gaurdPosition, gaurdDirection)}
            onMap = True
            loop = False
            while onMap and not loop:
                destination = (gaurdPosition[0] + gaurdDirection[0], gaurdPosition[1]+gaurdDirection[1])
                if -1 < destination[0] < mapHeight and -1 < destination[1] < mapLen:
                    if data[destination[0]][destination[1]] == "#":
                        gaurdDirection = gaurdDirectionRotation[gaurdDirection]
                        #print("destination is", data[destination[0]][destination[1]], "at", destination[0], destination[1])
                    else:
                        gaurdPosition = destination
                    toup = tuple([gaurdPosition, gaurdDirection])
                    #print(toup)
                    #print(type(toup))
                    inSetVar = toup in seenStates
                    if inSetVar:
                        loop = True
                        total = total + 1
                        # print("x is", xExtra, "y is", yExtra)
                        # print("state is", toup)
                        # print("seen states are", seenStates)
                    else:
                        seenStates.add(tuple([gaurdPosition, gaurdDirection]))

                else:
                    onMap = False
            data[yExtra][xExtra] = "."
            #print()
print(total)
