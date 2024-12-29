data = open("C:\\Users\\bcher\\OneDrive\\Desktop\\programs\\advent2024\\gitHub\\Advent2024\\19\\in.txt").read()
data = data.split("\n\n")

def getFirstFlase(list):
    for i in range(len(list)):
        if list[i][1] == False:
            return i
    return len(list)+1

def sortKey(listElem):
    return len(listElem[0])


data[0] = data[0].split(", ")
toMake = data[1].split("\n")
towlSet = set()
for towl in data[0]:
    towlSet.add(towl)

total = 0

for Pattern in toMake:
    thisSubPatters = [[Pattern, False]]
    seenSubPatterns = {Pattern:1}
    thisSubPattersIndex = 0
    while thisSubPattersIndex < len(thisSubPatters):
        currPatern = thisSubPatters[thisSubPattersIndex][0]
        thisSubPatters[thisSubPattersIndex][1] = True
        for PatternIndex in range(len(currPatern), 0, -1):
            if currPatern[0:PatternIndex] in towlSet:
                if currPatern[PatternIndex:] not in seenSubPatterns:
                    thisSubPatters.append([currPatern[PatternIndex:], False])
                    seenSubPatterns[currPatern[PatternIndex:]] = seenSubPatterns[currPatern]
                else:
                    seenSubPatterns[currPatern[PatternIndex:]] = seenSubPatterns[currPatern[PatternIndex:]] + seenSubPatterns[currPatern]
        thisSubPatters.sort(key=sortKey, reverse=True)
        thisSubPattersIndex = getFirstFlase(thisSubPatters)
    total = total + seenSubPatterns.get("", 0)

print(total)


