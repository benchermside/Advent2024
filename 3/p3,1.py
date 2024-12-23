data = open("C:\\Users\\bcher\\OneDrive\\Desktop\\programs\\advent2024\\3\\in.txt").read()
#print(len(data))
answer = 0
for i in range(len(data)):
    char = data[i]
    stillValid = True
    if data[i:i+4] == "mul(":
        allNum1 = ""
        indexAdd = i+4
        nonInt = False
        while not nonInt:
            # print(indexAdd)
            # print(data[indexAdd-8:indexAdd])
            if data[indexAdd] not in "1234567890":
                if data[indexAdd] != "," or allNum1 == "":
                    stillValid = False
                nonInt = True
            else:
                allNum1 = allNum1 + data[indexAdd]
            indexAdd = indexAdd + 1
        allNum2 = ""
        nonInt = False
        while not nonInt:
            if data[indexAdd] not in "1234567890":
                if data[indexAdd] != ")" or allNum2 == "":
                    stillValid = False
                nonInt = True
            else:
                allNum2 = allNum2 + data[indexAdd]
            indexAdd = indexAdd + 1
        if stillValid:
            answer = answer + (int(allNum2)*int(allNum1))
print(answer)

            
