data = open("C:\\Users\\bcher\\OneDrive\\Desktop\\programs\\advent2024\\gitHub\\Advent2024\\5\\in.txt").read()
data = data.split("\n")

found = False
i = 0
while not found:
    if data[i] == "":
        found = True
        splitIndex = i
    i = i + 1
dataRules = data[0:splitIndex]
dataPrints = data[splitIndex+1:]

for i in range(len(dataPrints)):
    dataPrints[i] = dataPrints[i].split(",")

for i in range(len(dataRules)):
    dataRules[i] = dataRules[i].split("|")

ruleGraphBefore = {}

for rule in dataRules:
    if not rule[0] in ruleGraphBefore:
        ruleGraphBefore[rule[0]] = {rule[1]}
    else:
        ruleGraphBefore[rule[0]].add(rule[1])

#print(ruleGraphBefore)


# for currCheck in ["99"]:
#     startList = list(ruleGraphBefore[currCheck])
#     addedNewList = []
#     while len(startList) > 0:
#         for elem in startList:
#             twoDegreeJumps = ruleGraphBefore.get(elem)
#             if twoDegreeJumps != None:
#                 for jump in twoDegreeJumps:
#                     if jump not in ruleGraphBefore[currCheck]:
#                         if jump == "31" and currCheck == "99":
#                             print("elem is", elem)
#                         ruleGraphBefore[currCheck].add(jump)
#                         addedNewList.append(jump)
#         startList = addedNewList
#         addedNewList = []


def sortList(list, table):
    if len(list)<2:
        return list
    lastElem = None
    for i in range(len(list)):
        currElem = list[i]
        currElemAfters = table[currElem]
        isLast = True
        for j in range(len(list)):
            if i != j:
                if list[j] in currElemAfters:
                    isLast = False
        if isLast:
            lastElem = currElem
            elemIndex = i
            break
    return sortList(list[0:elemIndex] + list[elemIndex+1:], table) + [lastElem]
    

total = 0
for line in dataPrints:
    followsRule = True
    lineLen = len(line)
    for i in range(lineLen-1):
        for j in range(i+1, lineLen):
            containsList = ruleGraphBefore.get(line[j])
            containsList2 = ruleGraphBefore.get(line[j])
            if containsList != None:
                if line[i] in containsList:
                    followsRule = False
        if not followsRule:
            break
    if not followsRule:
        #print("before", line)
        line = sortList(line, ruleGraphBefore)
        # for elemnum in range(lineLen):
        #     for elem2num in range(lineLen-1, elemnum, -1):
        #         containsList = ruleGraphBefore.get(line[elemnum])
        #         if containsList != None:
        #             if line[elemnum-1] in containsList:
        #                 #print("swaping ", line[elemnum-1], "and", line[elemnum])
        #                 temp = line[elemnum-1]
        #                 line[elemnum-1] = line[elemnum]
        #                 line[elemnum] = temp
        #print("after", line)
        total = total + int(line[(lineLen-1)//2])
print(total)


