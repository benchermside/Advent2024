data = open("C:\\Users\\bcher\\OneDrive\\Desktop\\programs\\advent2024\\6\\in.txt").read()
data = data.split("\n")
for i in range(len(data)):
    data[i] = list(data[i])

gaurdPosition = [None, None]
for y in range(len(data)):
    for x in range(len(data[y])):
        if data[y][x] == "^":
            gaurdPosition = [y, x]
            gaurdDirection = (-1, 0)
            data[y][x] = "X"
gaurdDirectionRotation = {(-1,0):(0,1), (0,1):(1,0), (1,0):(0,-1), (0,-1):(-1,0)}
mapLen = len(data[0])
mapHeight = len(data)
onMap = True
while onMap:
    data[gaurdPosition[0]][gaurdPosition[1]] = "X"
    destination = [gaurdPosition[0] + gaurdDirection[0], gaurdPosition[1]+gaurdDirection[1]]
    if -1 < destination[0] < mapHeight and -1 < destination[1] < mapLen:
        if data[destination[0]][destination[1]] == "#":
            gaurdDirection = gaurdDirectionRotation[gaurdDirection]
        else:
            gaurdPosition = destination
    else:
        onMap = False

total = 0
for row in data:
    for colum in row:
        total = total + (colum=="X")
print(total)
