from math import gcd

data = open("C:\\Users\\bcher\\OneDrive\\Desktop\\programs\\advent2024\\gitHub\\Advent2024\\13\\in.txt").read()
data = data.split("\n\n")

def addTouples(touple1, touple2):
    list = []
    for elem in range(len(touple1)):
        list.append(touple1[elem]+touple2[elem])
    return tuple(list)


for i in range(len(data)):
    data[i] = data[i].split("\n")

total = 0

for clawM in data:
    buttinA = clawM[0][10:].split(", ")
    buttinAX = int(buttinA[0][2:])
    buttinAY = int(buttinA[1][2:])
    buttinB = clawM[1][10:].split(", ")
    buttinBX = int(buttinB[0][2:])
    buttinBY = int(buttinB[1][2:])
    prize = clawM[2][7:].split(", ")
    prizeX = int(prize[0][2:])
    prizeY = int(prize[1][2:])
    try:
        y = (buttinAX*prizeY-buttinAY*prizeX)/(buttinAX*buttinBY-buttinAY*buttinBX)
        x = (prizeX-buttinBX*y)/buttinAX
        if x.is_integer() and y.is_integer():
            total = total + int(x)*3+int(y)
    except ZeroDivisionError:
        print("zero division error")
print(total)