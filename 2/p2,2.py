data = open("C:\\Users\\bcher\\OneDrive\\Desktop\\programs\\advent2024\\2\\in.txt").read()
splitData = data.split("\n")
for i in range(len(splitData)):
    splitData[i] = splitData[i].split(" ")
    for j in range(len(splitData[i])):
        splitData[i][j] = int(splitData[i][j])
#print(splitData)
count = 0
for line in splitData:
    anyThingWorks = False
    first = True
    second = True
    for i in range(1, len(line)):
        if not (line[i-1] < line[i] < line[i-1]+4):
            first = False
    for i in range(1, len(line)):
        if not (line[i-1]-4 < line[i] < line[i-1]):
            second = False
    anyThingWorks = first or second
    for i in range(len(line)):
        ThisList = line[0:i] + line[i+1:]
        first = True
        second = True
        for i in range(1, len(ThisList)):
            if not (ThisList[i-1] < ThisList[i] < ThisList[i-1]+4):
                first = False
        for i in range(1, len(ThisList)):
            if not (ThisList[i-1]-4 < ThisList[i] < ThisList[i-1]):
                second = False
        anyThingWorks = first or second or anyThingWorks
    count = count + anyThingWorks
print(count)

        
    



print(count)
