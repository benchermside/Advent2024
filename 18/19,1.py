data = open("C:\\Users\\bcher\\OneDrive\\Desktop\\programs\\advent2024\\gitHub\\Advent2024\\19\\in.txt").read()
data = data.split("\n\n")

data[0] = data[0].split(", ")
toMake = data[1].split("\n")
towlSet = set()
for towl in data[0]:
    towlSet.add(towl)

total = 0

for Pattern in toMake:
    thisSubPatters = [Pattern]
    thisSubPattersIndex = 0
    found = False
    while thisSubPattersIndex < len(thisSubPatters) and not found:
        currPatern = thisSubPatters[thisSubPattersIndex]
        for PatternIndex in range(1, len(currPatern)):
            if currPatern[0:PatternIndex] in towlSet:
                thisSubPatters.append(currPatern[PatternIndex:])
                if len(currPatern[PatternIndex:]) == 0:
                    found = True
        thisSubPattersIndex = thisSubPattersIndex + 1
    if found:
        total = total + 1

print(total)


