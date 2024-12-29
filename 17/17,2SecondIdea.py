desired = [2,4,1,3,7,5,4,1,1,3,0,3,5,5,3,0]
works = []
RB = 0
RC = 0
RA = 37283687
Outputs = []
#WorkingRAValues = []
for output in desired:
    works.append([])
    for RAValue in range(2**10):
        RA = RAValue
        Outputs = []
        #while RA != 0:
        while len(Outputs) == 0:
            RB = RA%8
            RB = RB^0b011
            RC = RA//(2**RB)#shift by RB
            RB = RB^RC
            RB = RB ^ 0b011
            RA = RA //(2**0b011)#shift by 3
            Outputs.append(RB%8)
        if Outputs[0] == output:
            works[-1].append(RAValue)


# print("works is", works[0])
# print("works 1 is", works[1])

totalFound = set()
for foundFirst in works[0]:
    totalFound.add(foundFirst)

for numIndex in range(1, len(works)):
    currList = works[numIndex]
    lowerCuts = {}
    for lowerCut in totalFound:
        if lowerCut >> (3*numIndex) in lowerCuts:
            lowerCuts[lowerCut >> (3*numIndex)].append(lowerCut)
        else:
            lowerCuts[lowerCut >> (3*numIndex)] = [lowerCut]
    newTotalFound = set()
    for upperCut in currList:
        middleOfCut = upperCut%(2**7)
        if middleOfCut in lowerCuts:
            for elem in lowerCuts[middleOfCut]:
                newTotalFound.add(elem + ((upperCut >> 7) << (7+3*numIndex)))
    totalFound = newTotalFound

# for val in totalFound:
#     print(val)
minVal = 9999999999999999999999999999999999999999
for val in totalFound:
    if 2**((len(desired)-1)*3) <= val < minVal and val < 2**((len(desired))*3):
        minVal = val
        print(val)
print(minVal)

