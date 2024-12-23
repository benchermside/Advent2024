data = open("C:\\Users\\bcher\\OneDrive\\Desktop\\programs\\advent2024\\5\\in.txt").read()
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
ruleGraphAfter = {}

for rule in dataRules:
    if not rule[0] in ruleGraphBefore:
        ruleGraphBefore[rule[0]] = {rule[1]}
    else:
        ruleGraphBefore[rule[0]].add(rule[1])
    # if not rule[1] in ruleGraphAfter:
    #     ruleGraphAfter[rule[1]] = [rule[0]]
    # else:
    #     ruleGraphAfter[rule[1]].append(rule[0])

total = 0
for line in dataPrints:
    followsRule = True
    for i in range(len(line)-1):
        for j in range(i+1, len(line)):
            containsList = ruleGraphBefore.get(line[j])
            if containsList != None:
                if line[i] in containsList:
                    followsRule = False
    if followsRule:
        total = total + int(line[(len(line)-1)//2])
print(total)


