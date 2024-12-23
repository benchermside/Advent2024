data = open("C:\\Users\\bcher\\OneDrive\\Desktop\\programs\\advent2024\\1\\in.txt").read()
splitData = data.split("\n")

list1 = []
list2 = []
for line in splitData:
    for i in range(len(line)):
        if line[i]==" ":
            list1.append(line[0:i])
            break
    for j in range(len(line)-1, -1, -1):
        if line[j]==" ":
            list2.append(line[j+1:])
            break

list1.sort(key=int)
list2.sort(key=int)
total = 0
for i in range(len(list1)):
    total = total + abs(int(list1[i])-int(list2[i]))
print("p1 result is", total)

list2frequs = {}
for entry in list2:
    if not entry in list2frequs:
        list2frequs[entry] = 1
    else:
        list2frequs[entry] = list2frequs[entry] + 1

total2 = 0
for entry in list1:
    if entry in list2frequs:
        total2 = total2 + int(entry)*list2frequs[entry]
print("second result is", total2)
