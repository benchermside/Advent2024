data = open("C:\\Users\\bcher\\OneDrive\\Desktop\\programs\\advent2024\\4\\in.txt").read()
data = data.split("\n")

def swap1(input):
    if input == "M":
        return "S"
    elif input == "S":
        return "M"
    else:
        return input

def makeNone(input):
    if input == "M" or input == "S":
        return input
    else:
        return None
        


total = 0
for row in range(1, len(data)-1):
    for colum in range(1, len(data[0])-1):
        if data[row][colum] == "A" and makeNone(data[row+1][colum+1]) == swap1(data[row-1][colum-1]) and makeNone(data[row+1][colum-1])==swap1(data[row-1][colum+1]):
            total = total + 1
print(total)
#print(2*total)
                