data = open("C:\\Users\\bcher\\OneDrive\\Desktop\\programs\\advent2024\\2\\in.txt").read()
splitData = data.split("\n")
for i in range(len(splitData)):
    splitData[i] = splitData[i].split(" ")
    for j in range(len(splitData[i])):
        splitData[i][j] = int(splitData[i][j])
#print(splitData)
count = 0
for line in splitData:
    first = True
    second = True
    for i in range(1, len(line)):
        if not (line[i-1] < line[i] < line[i-1]+4):
            first = False
    for i in range(1, len(line)):
        if not (line[i-1]-4 < line[i] < line[i-1]):
            second = False
    count = count + (first or second)
print(count)
    