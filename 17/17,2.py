data = open("C:\\Users\\bcher\\OneDrive\\Desktop\\programs\\advent2024\\gitHub\\Advent2024\\17\\in.txt").read()
data = data.split("\n\n")

registers = data[0].split("\n")
program = data[1][9:].split(",")

registerA = int(registers[0][12:])
registerB = int(registers[1][12:])
initalRB = registerB
registerC = int(registers[2][12:])
initalRC = registerC

for lineIndex in range(len(program)):
    program[lineIndex] = int(program[lineIndex])


headIndex = 0
outPut = []


def getComboValue(value):
    global registerA
    global registerB
    global registerC
    if value<4:
        return value
    elif value == 4:
        return registerA
    elif value == 5:
        return registerB
    elif value == 6:
        return registerC
    else:
        print("illegal state reached")

def adv(opp):
    global registerA
    comboVal = getComboValue(opp)
    registerA = registerA // (2**comboVal)
def bxl(opp):
    global registerB
    registerB = registerB ^ opp
def bst(opp):
    global registerB
    registerB = getComboValue(opp)%8
def jnz(opp):
    global registerA
    global headIndex
    if registerA != 0:
        headIndex = opp-2
def bxc(opp):
    global registerA
    global registerB
    global registerC
    registerB = registerB ^ registerC
def out(opp):
    outPut.append(getComboValue(opp)%8)
def bdv(opp):
    global registerA
    global registerB
    comboVal = getComboValue(opp)
    registerB = registerA // (2**comboVal)
def cdv(opp):
    global registerA
    global registerC
    comboVal = getComboValue(opp)
    registerC = registerA // (2**comboVal)
getFunct = [adv, bxl, bst, jnz, bxc, out, bdv, cdv]

firstVal = None
for regAval in range(2000000):
    registerA = regAval
    registerB = initalRB
    registerC = initalRC
    headIndex = 0
    outPut = []
    while headIndex < len(program):
        funk = getFunct[program[headIndex]]
        opp = program[headIndex+1]
        funk(opp)
        headIndex = headIndex + 2
    found = len(outPut) == len(program)
    if found:
        for elemIndex in range(len(outPut)):
            if outPut[elemIndex] != program[elemIndex]:
                found = False
        if found:
            firstVal = regAval
            break

                

print(firstVal)
